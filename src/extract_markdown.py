import re


def extract_markdown_images(markdown: str):
    # other option r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    image_alt_and_url_pattern = r"!\[([^\]]*)\]\(([^\)]*)\)"
    return re.findall(image_alt_and_url_pattern, markdown)


def extract_markdown_links(markdown: str):
    # fancy regex r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    link_name_and_url_pattern = r"[^!]\[([^\]]*)\]\(([^\)]*)\)"
    return re.findall(link_name_and_url_pattern, markdown)
