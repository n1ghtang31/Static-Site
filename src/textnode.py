from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode
class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE_TEXT = "code_text"
    LINKS = "links"
    IMAGES = "images"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, value):
        return self.text == value.text and self.text_type == value.text_type and self.url == value.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(TextNode):
    if TextNode.text_type == TextType.NORMAL:
        return LeafNode(None, TextNode.text)
    if TextNode.text_type == TextType.BOLD:
        return LeafNode("b", TextNode.text)
    if TextNode.text_type == TextType.ITALIC:
        return LeafNode("i", TextNode.text)
    if TextNode.text_type == TextType.CODE_TEXT:
        return LeafNode("code", TextNode.text)
    if TextNode.text_type == TextType.LINKS:
        return LeafNode("a", TextNode.text, {"href": TextNode.url})
    if TextNode.text_type == TextType.IMAGES:
        return LeafNode("img", None, {"src": TextNode.url, "alt": TextNode.text})
    else:
        raise ValueError("Invalid text type")
    


