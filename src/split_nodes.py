from .text_node import TextType, TextNode


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, new_type: TextType) -> list[TextNode]:
    if delimiter is None or delimiter == "":
        raise ValueError("Delimiter can't be null nor empty")
    if new_type is None:
        new_type = TextType.TEXT

    new_nodes = []

    for node in old_nodes:
        parts = node.text.split(delimiter)
        for i, part in enumerate(parts):
            text_type = new_type if i % 2 == 1 else node.text_type
            new_nodes.append(TextNode(text=part, text_type=text_type))

    return new_nodes
