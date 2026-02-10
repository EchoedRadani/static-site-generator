from textnode import TextNode, TextType
import os
import shutil


def copy_static_to_public(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)
        print(f" * {source_path} -> {destination_path}")
        if os.path.isdir(source_path):  
            copy_static_to_public(source_path, destination_path)
        else:
            shutil.copy2(source_path, destination_path)


def main():
    source = "./static"
    destination = "./public"
    copy_static_to_public(source, destination)

main()