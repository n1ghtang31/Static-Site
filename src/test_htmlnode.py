import unittest

from htmlnode import HTMLNode

class TestHtMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "Google", None, {"href": "https://www.google.com", "target": "_blank"})
        answer = node.props_to_html()
        self.assertEqual(answer, " href='https://www.google.com' target='_blank'")

        node2 = HTMLNode("div", "Oh god why", None, {"id": "wrapper", "class": "container"})
        answer2 = node2.props_to_html()
        self.assertEqual(answer2, " id='wrapper' class='container'")

    def test_props_to_html_none(self):
        node = HTMLNode("a", "Google", "")
        answer = node.props_to_html()
        self.assertEqual(answer, "")

    def test_repr(self):
        node = HTMLNode("a", "Google", "", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(repr(node), "HTMLNode(tag: a, value: Google, children: , props: {'href': 'https://www.google.com', 'target': '_blank'})")


if __name__ == "__main__":
    unittest.main()


