import unittest

from src.extract_markdown import \
    extract_markdown_images, \
    extract_markdown_links


class TestExtractMarkdown(unittest.TestCase):
    def setUp(self):
        self.simple_text = "This is a simple text"
        self.trappy_text = "This text [tries] to (fool you)\n Hah ![haha]"
        self.text_with_image = "This is text with an \
        ![image](https://i.imgur.com/zjjcJKZ.png)"
        self.text_with_link = "This is text with an \
        [link name](https://i.link.com)"
        self.text_with_multiple_images = "This is text with multiple images\n \
        this is one\n![alt1](https://images.com/image1.png)\nhere is another\n\
        ![alt2](https://images.com/image2.png) \n and here is yet another \n\
        ![alt3](https://images.com/image3.png)"
        self.text_with_multiple_links = "This is text with multiple links\n \
        this is one\n[name1](https://links1.com)\nhere is another\n\
        [name2](https://links2.com) \n and here is yet another \n\
        [name3](https://links3.com)"
        self.text_with_multiple_links_and_images = "This is text with \
        multiple images\n \
        this is one\n![alt1](https://images.com/image1.png)\nhere is another\n\
        ![alt2](https://images.com/image2.png) \n and here is yet another \n\
        ![alt3](https://images.com/image3.png) \n followed by text with \
        multiple links\n\
        this is one\n[name1](https://links1.com)\nhere is another\n\
        [name2](https://links2.com) \n and here is yet another \n\
        [name3](https://links3.com)"

    def test_extract_markdown_images(self):
        # test with only one match in text
        matches = extract_markdown_images(
            self.text_with_image
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

        # test with simple text
        matches = extract_markdown_images(
            self.simple_text
        )
        self.assertListEqual([], matches)

        # test with a trappy string
        matches = extract_markdown_links(
            self.trappy_text
        )
        self.assertListEqual([], matches)

        # test with link instead of images
        matches = extract_markdown_images(
            self.text_with_link
        )
        self.assertListEqual([], matches)

        # test with multiple images
        matches = extract_markdown_images(
            self.text_with_multiple_images
        )
        self.assertListEqual(
            [
                ("alt1", "https://images.com/image1.png"),
                ("alt2", "https://images.com/image2.png"),
                ("alt3", "https://images.com/image3.png")
            ],
            matches
        )

        # test with mixed linkes and images
        matches = extract_markdown_images(
            self.text_with_multiple_links_and_images
        )
        self.assertListEqual(
            [
                ("alt1", "https://images.com/image1.png"),
                ("alt2", "https://images.com/image2.png"),
                ("alt3", "https://images.com/image3.png")
            ],
            matches
        )

    def test_extract_empty_markdown_images(self):
        # test with an empty string
        matches = extract_markdown_images("")
        self.assertListEqual([], matches)

    def test_extract_markdown_links(self):
        # test with text with one single link
        matches = extract_markdown_links(
            self.text_with_link
        )
        self.assertListEqual(
            [("link name", "https://i.link.com")], matches)

        # test for simple text with no images/liks
        matches = extract_markdown_links(
            self.simple_text
        )
        self.assertListEqual([], matches)

        # test with a trappy string
        matches = extract_markdown_links(
            self.trappy_text
        )
        self.assertListEqual([], matches)

        # test with an image instead of a link
        matches = extract_markdown_links(
            self.text_with_image
        )
        self.assertListEqual([], matches)

        # Test multiple links
        matches = extract_markdown_links(
            self.text_with_multiple_links
        )
        self.assertListEqual(
            [
                ("name1", "https://links1.com"),
                ("name2", "https://links2.com"),
                ("name3", "https://links3.com")
            ],
            matches
        )

        # test with mixed links and images
        matches = extract_markdown_links(
            self.text_with_multiple_links_and_images
        )
        self.assertListEqual(
            [
                ("name1", "https://links1.com"),
                ("name2", "https://links2.com"),
                ("name3", "https://links3.com")
            ],
            matches
        )

    def test_extract_empty_markdown_links(self):
        # test with an empty string
        matches = extract_markdown_links("")
        self.assertListEqual([], matches)
