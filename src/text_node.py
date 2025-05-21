from __future__ import annotations
from enum import Enum
from src.html_node import HTMLNode, LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(
        self,
        text: str | None = None,
        text_type: TextType | None = None,
        url: str = None
    ):
        if text_type not in TextType:
            raise ValueError("Invalid textType")
        if text_type == TextType.IMAGE or text_type == TextType.LINK:
            if url is None:
                raise ValueError("URL cannot be None for IMAGES and LINKS")
        elif url is not None:
            raise ValueError("URL can be set only for IMAGES and LINKS")

        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, otherTextNode: TextNode):
        return (
            self.text == otherTextNode.text and
            self.text_type == otherTextNode.text_type and
            self.url == otherTextNode.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, \
        {
            self.text_type.value
            if self.text_type.value is not None and self.text_type in TextType
            else None
        }, \
        {self.url})"

    def to_html_node(self) -> HTMLNode:
        if self.text_type not in TextType:
            raise ValueError(f"Invalid text_type {self.textType}")
        if self.text_type == TextType.TEXT:
            return LeafNode(None, self.text)
        if self.text_type == TextType.BOLD:
            return LeafNode("b", self.text)
        if self.text_type == TextType.ITALIC:
            return LeafNode("i", self.text)
        if self.text_type == TextType.CODE:
            return LeafNode("code", self.text)
        if self.text_type == TextType.LINK:
            return LeafNode("a", self.text, {"href": self.url})
        if self.text_type == TextType.IMAGE:
            return LeafNode("img", None, {"src": self.url, "alt": self.text})
