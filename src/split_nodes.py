from src.text_node import TextType, TextNode
from src.extract_markdown \
    import extract_markdown_links, extract_markdown_images


def split_nodes_delimiter(
        old_nodes: list[TextNode],
        delimiter: str,
        new_type: TextType
) -> list[TextNode]:
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


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        node_text = node.text
        for image_alt, image_url in extract_markdown_images(node_text):
            parts = node_text.split(f"![{image_alt}]({image_url})", 1)
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))
            node_text = parts[1] if len(parts) == 2 else ""
        if node_text != "":
            new_nodes.append(TextNode(node_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        node_text = node.text
        for link_name, link_url in extract_markdown_links(node_text):
            parts = node_text.split(f"[{link_name}]({link_url})", 1)
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(link_name, TextType.IMAGE, link_url))
            node_text = parts[1] if len(parts) == 2 else ""
        if node_text != "":
            new_nodes.append(TextNode(node_text, TextType.TEXT))
    return new_nodes
