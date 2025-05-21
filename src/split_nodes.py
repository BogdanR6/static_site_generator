from .text_node import TextType, TextNode


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, new_type: TextType) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        parts = node.text.split(delimiter)
        for i, part in enumerate(parts):
            text_type = new_type if i % 2 == 1 else node.text_type
            new_nodes.append(TextNode(text=part, text_type=text_type))

    return new_nodes
