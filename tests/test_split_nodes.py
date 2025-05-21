import unittest

from src.text_node import TextNode, TextType
from src.split_nodes import split_nodes_delimiter


class TestSplitNodes(unittest.TestCase):
    def setUp(self):
        self.node = TextNode(
            "This is text with a `code block` word", TextType.TEXT)

    def tearDown(self):
        del self.node

    def test_split(self):
        newNodes = split_nodes_delimiter([self.node], "`", TextType.CODE)
        self.assertEqual(
            newNodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        )
