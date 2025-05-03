from __future__ import annotations


class HTMLNode:
    def __init__(
            self,
            tag: str | None = None,
            value: str | None = None,
            children: list[HTMLNode] | None = None,
            props: dict[str, str] | None = None
    ):
        if tag is None and props is not None:
            raise ValueError("Node with no tag can't have props")
        if value is None and children is None:
            raise ValueError("Node must have either a value or a child")
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def toHTML(self):
        raise NotImplementedError

    def propsToHtml(self) -> str:
        if self.props is None:
            return ""
        html = ""
        for key, value in self.props:
            html += f' {key}="{value}"'
        return html

    def __repr__(self):
        return f'<{str(self.children)}> \
        <{self.tag}{self.propsToHtml()}>{self.value}<{self.tag}>'
