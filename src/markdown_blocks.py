import re

#Types of blocks
block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
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
            if not line.startswith("* ") or line.startswith("- "):
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
    
