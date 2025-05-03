from __future__ import annotations
from enum import Enum


class TextType(Enum):
    NORMAL = "normal"
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
        if url is None:
            raise ValueError("URL cannot be None")
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
        {self.textType.value if self.textType.value is not None else None}, \
        {self.url})"
