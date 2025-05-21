import unittest

from src.text_node import TextNode, TextType
from src.split_nodes import split_nodes_delimiter


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
