import os
from block_markdown import markdown_to_html_node


def extract_title(markdown):
    if not markdown.startswith("# "):
        raise Exception("markdown does not start with an h1 heading")
    get_title_line = markdown[2:].split("\n")
    title = get_title_line[0]
    return title


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as markdown_file, open(template_path, "r") as template_file:
        read_markdown_file = markdown_file.read()
        read_template_file = template_file.read()
    to_html_node = markdown_to_html_node(read_markdown_file)
    html_string = to_html_node.to_html()
    title = extract_title(read_markdown_file)
    replace = read_template_file.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, "w") as new_html:
        new_html.write(replace)