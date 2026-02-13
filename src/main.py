import os
import shutil
from generate_page import generate_page


def copy_static_to_public(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)
        print(f" * {source_path} -> {destination_path}")
        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
        else:
            copy_static_to_public(source_path, destination_path)

static_source = "./static"
page_source = "./content/index.md"
static_destination = "./public"
page_destination = "./public/index.html"
template = "template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(static_destination):
        shutil.rmtree(static_destination)
    copy_static_to_public(static_source, static_destination)
    generate_page(page_source, template, page_destination)


main()