import os
import shutil
from generate_page import generate_pages_recursive


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

dir_static_path = "./static"
dir_public_path = "./public"
dir_page_content = "./content"
template = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_public_path):
        shutil.rmtree(dir_public_path)
    print("Copying static files to public directory...")
    copy_static_to_public(dir_static_path, dir_public_path)
    print("Generating content...")
    generate_pages_recursive(dir_page_content, template, dir_public_path)

main()