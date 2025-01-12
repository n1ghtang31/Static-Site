import re
from htmlnode import LeafNode, ParentNode
from textnode import TextNode, text_node_to_html_node
from inline_markdown import text_to_textnodes, TextNode, TextType

#Types of blocks
block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "blockquote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"


def markdown_to_blocks(markdown):
    split_markdown = markdown.split("\n\n")
    #cleaning out extra whitespace and empty blocks
    cleaned_markdown = [block.strip() for block in split_markdown if block.strip()]
    return cleaned_markdown

def block_to_block_type(block):
    lines = block.split("\n")
    #Check if heading
    if re.match(r"(#{1,6}).+", block):
        return block_type_heading
    #Check if code
    elif len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    #Check if quote
    elif block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    #check if an unordered list
    elif block.startswith("- ") or block.startswith("* "):
        for line in lines:
            if not (line.startswith("* ") or line.startswith("- ")):
                return block_type_paragraph
        return block_type_ulist
    #check if an ordered list
    elif block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    #if none of the above are true will be returned as normal text
    else:
        return block_type_paragraph
    

#This is a fucking mess but it seems to work
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        type = block_to_block_type(block)
        match type:
            case str() if type == block_type_quote:
                split_lines = block.split("\n")
                list_lines = []
                for line in split_lines:
                    if line.startswith("> "):
                        line = line[2:]
                    list_lines.append(line)
                joined_nodes = " ".join(list_lines)
                block = LeafNode(block_type_quote, joined_nodes)
                nodes.append(block)
            case str() if type == block_type_heading:
                match = re.match(r"(#{1,6})\s*(.+)", block)
                if match:
                    heading_level = len(match.group(1))
                    heading_text = match.group(2)
                    heading_node = LeafNode(f"h{heading_level}", heading_text)
                    nodes.append(heading_node)
            case str() if type == block_type_code:
                block = LeafNode(block_type_code, block)
                parent = ParentNode("pre", block)
                nodes.append(parent)
            case str() if type == block_type_olist:
                split_lines = block.split('\n')
                list_lines = []
                for line in split_lines:
                    line = line[3:]
                    child_list = []
                    children = text_to_textnodes(line)
                    if isinstance(children, list):
                        for child in children:
                            child_list.append(text_node_to_html_node(child))
                    else:
                        child_list.append(text_node_to_html_node(children))
                    line = ParentNode("li", child_list)
                    
                    list_lines.append(line)
                parent = ParentNode("ol", list_lines)
                nodes.append(parent)
            case str() if type == block_type_ulist:
                split_lines = block.split('\n')
                list_lines = []
                for line in split_lines:
                    line = line[2:]
                    child_list = []
                    children = text_to_textnodes(line)
                    if isinstance(children, list):
                        for child in children:
                            child_list.append(text_node_to_html_node(child))
                    else:
                        child_list.append(text_node_to_html_node(children))
                    line = ParentNode("li", child_list)
                    
                    list_lines.append(line)
                parent = ParentNode("ul", list_lines)
                nodes.append(parent)
            case str() if type == block_type_paragraph:
                split_lines = block.split('\n')
                joined_lines = " ".join(split_lines)
                text_nodes = text_to_textnodes(joined_lines)
                if isinstance(text_nodes, TextNode):
                    text_nodes= [text_nodes]
                children = []
                for text_node in text_nodes:
                    html_node = text_node_to_html_node(text_node)
                    children.append(html_node)
                
                parent = ParentNode("p", children)
                nodes.append(parent)
                
            case _:
                block = text_to_textnodes(block)
                block = text_node_to_html_node(block)
                nodes.append(block)
    div_node = ParentNode("div", nodes)
    return div_node



