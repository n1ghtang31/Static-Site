import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_leaf_node_to_html(self):
        node = LeafNode("a", "Google", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), "<a href='https://www.google.com' target='_blank'>Google</a>")

    def test_leaf_node_to_html_no_value(self):
        node = LeafNode("a", None, {"href": "https://www.google.com", "target": "_blank"})
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_node_repr(self):
        node = LeafNode("a", "Google", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(repr(node), "LeafNode(tag: a, value: Google, children: None, props: {'href': 'https://www.google.com', 'target': '_blank'})")

    def test_parent_node_to_html(self):
        child = LeafNode("a", "Google", {"href": "https://www.google.com", "target": "_blank"})
        parent = ParentNode("div", [child], {"id": "wrapper", "class": "container"})
        self.assertEqual(parent.to_html(), "<div id='wrapper' class='container'><a href='https://www.google.com' target='_blank'>Google</a></div>")


if __name__ == "__main__":
    unittest.main()


