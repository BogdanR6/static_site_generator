import unittest

from src.html_node import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def setUp(self):
        self.htmlNode1 = HTMLNode("h1", "Title")
        self.htmlNode2 = HTMLNode("p", "This is a paragraph")
        self.htmlNode3 = HTMLNode("a", "This is a link", props={
                                  "href": "exemple.com", "target": "_blank"})
        self.htmlNode4 = HTMLNode(
            "div", children=[self.htmlNode1, self.htmlNode2, self.htmlNode3])
        self.htmlNode5 = HTMLNode("h2", "Title2")
        self.htmlNode6 = HTMLNode("footer", children=[self.htmlNode5])

    def tearDown(self):
        del self.htmlNode1
        del self.htmlNode2
        del self.htmlNode3
        del self.htmlNode4
        del self.htmlNode5
        del self.htmlNode6

    def test_constructor(self):
        self.assertEqual(self.htmlNode1.tag, "h1")
        self.assertEqual(self.htmlNode1.value, "Title")
        self.assertEqual(self.htmlNode1.children, None)
        self.assertEqual(self.htmlNode1.props, None)

        self.assertEqual(self.htmlNode2.tag, "p")
        self.assertEqual(self.htmlNode2.value, "This is a paragraph")
        self.assertEqual(self.htmlNode2.children, None)
        self.assertEqual(self.htmlNode2.props, None)

        self.assertEqual(self.htmlNode3.tag, "a")
        self.assertEqual(self.htmlNode3.value, "This is a link")
        self.assertEqual(self.htmlNode3.children, None)
        self.assertEqual(self.htmlNode3.props, {
                         "href": "exemple.com", "target": "_blank"})

        self.assertEqual(self.htmlNode4.tag, "div")
        self.assertEqual(self.htmlNode4.value, None)
        self.assertEqual(self.htmlNode4.children, [
                         self.htmlNode1, self.htmlNode2, self.htmlNode3])
        self.assertEqual(self.htmlNode4.props, None)

        self.assertEqual(self.htmlNode5.tag, "h2")
        self.assertEqual(self.htmlNode5.value, "Title2")
        self.assertEqual(self.htmlNode5.children, None)
        self.assertEqual(self.htmlNode5.props, None)

        self.assertEqual(self.htmlNode6.tag, "footer")
        self.assertEqual(self.htmlNode6.value, None)
        self.assertEqual(self.htmlNode6.children, [self.htmlNode5])
        self.assertEqual(self.htmlNode6.props, None)

    def test_constructor_exception(self):
        try:
            HTMLNode(None, "Value", [], {"style": "background-color: green;"})
            self.assertTrue(False)
        except ValueError:
            pass

    def test_props_to_html(self):
        self.assertEqual(self.htmlNode3.props_to_html(),
                         ' href="exemple.com" target="_blank"')
        self.assertEqual(self.htmlNode1.props_to_html(), '')

    def test_leafto_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_parent_to_html_with_children(self):
        leafNode1 = LeafNode("p", "paragraph!")
        leafNode2 = LeafNode("a", "link!")
        leafNode3 = LeafNode("b", "bold!")
        leafNode4 = LeafNode("i", "italic!")
        leafNode5 = LeafNode(None, "plain!")
        parentNode1 = ParentNode("div", [
            leafNode1,
            leafNode2,
            leafNode3,
            leafNode4,
            leafNode5
        ])
        self.assertEqual(
            parentNode1.to_html(),
            "<div><p>paragraph!</p><a>link!</a><b>bold!</b><i>italic!</i>plain!</div>"
        )

    def test_parent_to_html_with_grandchildren(self):
        leafNode1 = LeafNode("p", "paragraph!")
        leafNode2 = LeafNode("a", "link!")
        leafNode3 = LeafNode("b", "bold!")
        leafNode4 = LeafNode("i", "italic!")
        leafNode5 = LeafNode(None, "plain!")
        parentNode1 = ParentNode("div", [
            leafNode1,
            leafNode2,
            leafNode3,
            leafNode4,
            leafNode5
        ])
        parentNode2 = ParentNode("p", [
            parentNode1
        ])
        self.assertEqual(
            parentNode2.to_html(),
            "<p><div><p>paragraph!</p><a>link!</a><b>bold!</b><i>italic!</i>plain!</div></p>"
        )

    def test_parent_to_html_with_no_children(self):
        try:
            ParentNode("div", []).to_html()
            self.assertTrue(False)
        except ValueError:
            pass

        try:
            ParentNode("div", None).to_html()
            self.assertTrue(False)
        except ValueError:
            pass

    def test_parent_to_html_with_no_tag(self):
        try:
            ParentNode("", [HTMLNode()]).to_html()
            self.assertTrue(False)
        except ValueError:
            pass

        try:
            ParentNode(None, [HTMLNode()]).to_html()
            self.assertTrue(False)
        except ValueError:
            pass
