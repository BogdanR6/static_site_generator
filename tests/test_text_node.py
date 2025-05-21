import unittest
from src.text_node import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node1 = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

        node3 = TextNode("This is a text node", TextType.BOLD)
        node4 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node3, node4)

        node5 = TextNode("This is a text node", TextType.BOLD)
        node6 = TextNode("This is another text node", TextType.ITALIC)
        self.assertNotEqual(node5, node6)

    def test_constructor(self):
        text = "This is a text node"
        type = TextType.IMAGE
        url = "URL"

        node = TextNode(text, type, url)
        self.assertEqual(node.text, text)
        self.assertEqual(node.text_type, type)
        self.assertEqual(node.url, url)

    def test_constructor_exception(self):
        text = "This is text"
        type = TextType.IMAGE

        # expect exception as url is null for image
        try:
            TextNode(text, type)
            self.assertTrue(False)
        except ValueError:
            pass

        # expect exception as url is null for link
        type2 = TextType.LINK
        try:
            TextNode(text, type2)
            self.assertTrue(False)
        except ValueError:
            pass

    def test_to_html_node_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        htmlNode = node.to_html_node()
        self.assertEqual(htmlNode.tag, None)
        self.assertEqual(htmlNode.value, "This is a text node")

    def test_to_html_node_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        htmlNode = node.to_html_node()
        self.assertEqual(htmlNode.tag, "b")
        self.assertEqual(htmlNode.value, "This is a bold node")

    def test_to_html_node_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        htmlNode = node.to_html_node()
        self.assertEqual(htmlNode.tag, "i")
        self.assertEqual(htmlNode.value, "This is an italic node")

    def test_to_html_node_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        htmlNode = node.to_html_node()
        self.assertEqual(htmlNode.tag, "code")
        self.assertEqual(htmlNode.value, "This is a code node")

    def test_to_html_node_link(self):
        node = TextNode("This is a link node", TextType.LINK, "link")
        htmlNode = node.to_html_node()
        self.assertEqual(htmlNode.tag, "a")
        self.assertEqual(htmlNode.value, "This is a link node")
        self.assertEqual(htmlNode.props, {"href": "link"})

    def test_to_html_node_image(self):
        node = TextNode("This is alt text", TextType.IMAGE, "imageLink")
        htmlNode = node.to_html_node()
        self.assertEqual(htmlNode.tag, "img")
        self.assertEqual(htmlNode.value, None)
        self.assertEqual(htmlNode.props, {
                         "src": "imageLink", "alt": "This is alt text"})


if __name__ == "__main__":
    unittest.main()
