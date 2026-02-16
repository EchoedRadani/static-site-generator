import os
from block_markdown import markdown_to_html_node


def extract_title(markdown):
    if not markdown.startswith("# "):
        raise Exception("markdown does not start with an h1 heading")
    get_title_line = markdown[2:].split("\n")
    title = get_title_line[0]
    return title


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as markdown_file, open(template_path, "r") as template_file:
        read_markdown_file = markdown_file.read()
        read_template_file = template_file.read()
    to_html_node = markdown_to_html_node(read_markdown_file)
    html_string = to_html_node.to_html()
    title = extract_title(read_markdown_file)
    replace = read_template_file.replace("{{ Title }}", title).replace("{{ Content }}", html_string).replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, "w") as new_html:
        new_html.write(replace)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for file in os.listdir(dir_path_content):
        source_path = os.path.join(dir_path_content, file)
        dest_path = os.path.join(dest_dir_path, file)
        if os.path.isfile(source_path):
            html_name = file.replace(".md", ".html")
            final_dest = os.path.join(dest_dir_path, html_name)
            generate_page(source_path, template_path, final_dest, basepath)
        else:
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(source_path, template_path, dest_path, basepath)