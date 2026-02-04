from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        delimiter_split = node.text.split(delimiter)

        if (len(delimiter_split) - 1) % 2 == 1:
            raise Exception(f"missing par delimiter for: {delimiter}")
    
        for i in range(len(delimiter_split)):
            if delimiter_split[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(delimiter_split[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(delimiter_split[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes