import unittest

from src.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "URL")
        node2 = TextNode("This is a text node", TextType.BOLD, "URL")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node1 = TextNode("This is a text node", TextType.ITALIC, "URL")
        node2 = TextNode("This is a text node", TextType.BOLD, "URL")
        self.assertNotEqual(node1, node2)

        node3 = TextNode("This is a text node", TextType.BOLD, "URL")
        node4 = TextNode("This is another text node", TextType.BOLD, "URL")
        self.assertNotEqual(node3, node4)

        node5 = TextNode("This is a text node", TextType.BOLD, "URL1")
        node6 = TextNode("This is another text node", TextType.ITALIC, "URL2")
        self.assertNotEqual(node5, node6)

    def test_constructor(self):
        text = "This is a text node"
        type = TextType.BOLD
        url = "URL"

        node = TextNode(text, type, url)
        self.assertEqual(node.text, text)
        self.assertEqual(node.textType, type)
        self.assertEqual(node.url, url)

    def test_constructor_exception(self):
        text = "This is a text node"
        type = TextType.BOLD

        # expect exception as url is null
        try:
            _ = TextNode(text, type)
            self.assertTrue(False)
        except ValueError:
            pass


if __name__ == "__main__":
    unittest.main()
