from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stipped_blocks = []
    for block in blocks:
        if block == "":
            continue
        stipped_blocks.append(block.strip())
    return stipped_blocks


def block_to_block_type(block):
    if is_code_block(block):
        return BlockType.CODE
    elif is_heading(block):
        return BlockType.HEADING
    elif is_quote(block):
        return BlockType.QUOTE
    elif is_unordered_list(block):
        return BlockType.UNORDERED_LIST
    elif is_ordered_list(block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    

def is_code_block(block):
    pass


def is_heading(block):
    pass


def is_quote(block):
    pass


def is_unordered_list(block):
    pass


def is_ordered_list(block):
    pass