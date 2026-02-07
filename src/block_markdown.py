from enum import Enum
from block_type_functions import (
    is_code_block,
    is_heading,
    is_quote,
    is_unordered_list,
    is_ordered_list,
    get_ordered_list_number
)


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
    if is_heading(block):
        return BlockType.HEADING
    if is_quote(block):
        return BlockType.QUOTE
    lines = block.split("\n")
    expected = 1
    found_ordered = False
    found_unordered = False
    for line in lines:
        if is_unordered_list(line):
            if found_ordered:
                return BlockType.PARAGRAPH
            found_unordered = True
        elif is_ordered_list(line):
            if found_unordered:
                return BlockType.PARAGRAPH
            found_ordered = True
            num = get_ordered_list_number(line)
            if num != expected:
                return BlockType.PARAGRAPH
            expected += 1
        else:
            return BlockType.PARAGRAPH
    if found_unordered:
        return BlockType.UNORDERED_LIST
    elif found_ordered:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH