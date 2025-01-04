import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")
    
    def test_repr_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://www.google.com")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, http://www.google.com)")

    def test_text_node_to_html_node_normal(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertIsNone(html_node.tag)

if __name__ == "__main__":
    unittest.main()