import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_text = old_node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise Exception("Wrong Markdown Formatting")
        for i in range(len(split_text)):
            if split_text[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(split_text[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(split_text[i], text_type))

    return new_nodes
            

def extract_markdown_images(text):
    pattern = r'!\[([^\[\]]*)\]\(([^\(\)]*)\)'
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)'
    matches = re.findall(pattern, text)
    return matches

#regex to see both:  !\[([^\]]+)\]\(([^\)]+)\)
#regex to see only in the []: !\[([^\]]+)\]


def split_nodes_image(old_nodes):
    new_nodes = []
    try:
        iter(old_nodes)
        if isinstance(old_nodes, str):
            old_nodes = [old_nodes]
    except TypeError:
        old_nodes = [old_nodes]
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        matches = extract_markdown_images(old_node.text)
        if matches == []:
            new_nodes.append(old_node)
            continue
            
        original_text = old_node.text
        last_end = 0
        
        for match in matches:
            # Construct the full markdown pattern from the match
            full_pattern = f"![{match[0]}]({match[1]})"
            # Find where this pattern occurs in the original text
            start = original_text.find(full_pattern, last_end)
            end = start + len(full_pattern)
            alt_text = match[0]
            image_link = match[1]
            
            # Add text before match
            if start > last_end:
                new_nodes.append(TextNode(original_text[last_end:start], TextType.TEXT))
                
                
            # Add the image markdown
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, image_link))
            
            last_end = end
            
        # Add remaining text
        if last_end < len(original_text):
            new_nodes.append(TextNode(original_text[last_end:], TextType.TEXT))
            
    return new_nodes    

def split_nodes_link(old_nodes):
    new_nodes = []
    try:
        iter(old_nodes)
        if isinstance(old_nodes, str):
            old_nodes = [old_nodes]
    except TypeError:
        old_nodes = [old_nodes]
    for old_node in old_nodes:

        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        matches = extract_markdown_links(old_node.text)

        if matches == []:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        last_end = 0

        for match in matches:
            link_text = match[0]
            link_url = match[1]
            full_pattern = f"[{link_text}]({link_url})"

            start = original_text.find(full_pattern, last_end)
            end = start + len(full_pattern)


            if start > last_end:
                new_nodes.append(TextNode(original_text[last_end:start], TextType.TEXT))


            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

            last_end = end
        
        if last_end < len(original_text):
            new_nodes.append(TextNode(original_text[last_end:], TextType.TEXT))

    return new_nodes



def text_to_textnodes(init_text):
        nodes = TextNode(init_text, "text")
        nodes = split_nodes_image(nodes)
        nodes = split_nodes_link(nodes)
        nodes = split_nodes_delimiter(nodes, "**", "bold")
        nodes = split_nodes_delimiter(nodes, "*", "italic")
        nodes = split_nodes_delimiter(nodes, "`", "code")
        if len(nodes) <= 1:
            nodes = nodes[0]
        return nodes



