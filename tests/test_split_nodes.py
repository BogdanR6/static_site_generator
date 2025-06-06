import unittest

from src.text_node import TextNode, TextType
from src.split_nodes \
    import split_nodes_delimiter, split_nodes_image, split_nodes_link


class TestSplitNodes(unittest.TestCase):
    def setUp(self):
        self.code_node = TextNode(
            "This is text with a `code block` word", TextType.TEXT)
        self.code_node2 = TextNode(
            "This is text with a `another code block` word", TextType.TEXT)
        self.code_node3 = TextNode(
            "This is text with a `yet another code block` word", TextType.TEXT)

    def tearDown(self):
        del self.code_node
        del self.code_node2
        del self.code_node3

    def test_no_delimiter_error(self):
        try:
            split_nodes_delimiter([self.code_node], "", TextType.CODE)
            self.assertTrue(False)
        except ValueError:
            pass

        try:
            split_nodes_delimiter([self.code_node], None, TextType.CODE)
            self.assertTrue(False)
        except ValueError:
            pass

    def test_empty_split(self):
        self.assertEqual([], split_nodes_delimiter([], "`", TextType.TEXT))
        self.assertEqual([], split_nodes_delimiter([], "`", None))

    def test_single_el_split(self):
        self.assertEqual(
            split_nodes_delimiter([self.code_node], "`", TextType.CODE),
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        )

    def test_multiple_el_split(self):
        self.assertEqual(
            split_nodes_delimiter(
                [
                    self.code_node,
                    self.code_node2,
                    self.code_node3
                ],
                "`",
                TextType.CODE
            ),
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("another code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("yet another code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        )

    def test_split_images(self):
        node = TextNode(
            (
                "This is text with an "
                "![image](https://i.imgur.com/zjjcJKZ.png) "
                "and another ![second image](https://i.imgur.com/3elNhQu.png)"
            ),
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE,
                         "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image",
                    TextType.IMAGE,
                    "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            (
                "This is text with an "
                "[link](https://i.imgur.com/zjjcJKZ) "
                "and another [second link](https://i.imgur.com/3elNhQu)"
            ),
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.IMAGE,
                         "https://i.imgur.com/zjjcJKZ"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link",
                    TextType.IMAGE,
                    "https://i.imgur.com/3elNhQu"
                ),
            ],
            new_nodes,
        )
