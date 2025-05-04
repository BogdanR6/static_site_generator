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

    def toHTML(self) -> str:
        raise NotImplementedError

    def propsToHtml(self) -> str:
        if self.props is None:
            return ""
        html = ""
        for key, value in self.props.items():
            html += f' {key}="{value}"'
        return html

    def __repr__(self):
        return f'<{str(self.children)}> \
        <{self.tag}{self.propsToHtml()}>{self.value}<{self.tag}>'


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str | None,
        value: str,
        props: dict[str, str] | None = None
    ):
        super().__init__(tag, value, None, props)

    def toHTML(self) -> str:
        if self.value is None:
            raise ValueError("LeafNode has no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.propsToHtml()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: [HTMLNode],
        props: dict[str, str] | None = None
    ):
        super().__init__(tag, None, children, props)

    def toHTML(self) -> str:
        if self.tag is None or self.tag == '':
            raise ValueError("Invalid tag for parent node")
        if self.children is None or self.children == []:
            raise ValueError(
                "children must be a non empty list of HTMLNodes for ParentNode"
            )
        childHtml = ""
        for child in self.children:
            childHtml += child.toHTML()
        return f"<{self.tag}{self.propsToHtml()}>{childHtml}</{self.tag}>"
