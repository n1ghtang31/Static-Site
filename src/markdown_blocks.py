def markdown_to_blocks(markdown):
    split_markdown = markdown.split("\n\n")
    #cleaning out extra whitespace and empty blocks
    cleaned_markdown = [block.strip() for block in split_markdown if block.strip()]
    return cleaned_markdown







test_case = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.





* This is the first list item in a list block
* This is a list item
* This is another list item       """

print(markdown_to_blocks(test_case))