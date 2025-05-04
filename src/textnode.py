from __future__ import annotations
from enum import Enum
from src.htmlnode import HTMLNode, LeafNode


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
        textType: TextType | None = None,
        url: str = None
    ):
        if textType not in TextType:
            raise ValueError("Invalid textType")
        if textType == TextType.IMAGE or textType == TextType.LINK:
            if url is None:
                raise ValueError("URL cannot be None for IMAGES and LINKS")
        elif url is not None:
            raise ValueError("URL can be set only for IMAGES and LINKS")

        self.text = text
        self.textType = textType
        self.url = url

    def __eq__(self, otherTextNode: TextNode):
        return (
            self.text == otherTextNode.text and
            self.textType == otherTextNode.textType and
            self.url == otherTextNode.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, \
        {
            self.textType.value
            if self.textType.value is not None and self.textType in TextType
            else None
        }, \
        {self.url})"

    def toHTMLNode(self) -> HTMLNode:
        if self.textType not in TextType:
            raise ValueError(f"Invalid textType {self.textType}")
        if self.textType == TextType.TEXT:
            return LeafNode(None, self.text)
        if self.textType == TextType.BOLD:
            return LeafNode("b", self.text)
        if self.textType == TextType.ITALIC:
            return LeafNode("i", self.text)
        if self.textType == TextType.CODE:
            return LeafNode("code", self.text)
        if self.textType == TextType.LINK:
            return LeafNode("a", self.text, {"href": self.url})
        if self.textType == TextType.IMAGE:
            return LeafNode("img", None, {"src": self.url, "alt": self.text})
