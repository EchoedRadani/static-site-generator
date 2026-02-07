def is_code_block(block):
    if block.startswith("```\n") and block.endswith("\n```"):
        midde = block[4:-3]
        stripped_middle = midde.strip()
        return len(stripped_middle) > 0
    return False


def is_heading(block):
    if block.startswith("#"):
        check_lines = block.split("\n")
        if len(check_lines) == 1:
            line = check_lines[0]
            count = 0
            for letter in line:
                if letter == "#":
                    count += 1
                else:
                    break
            if len(line) > count + 1:
                line_space = line[count]
                text = line[count + 1:]
                is_line_space = line_space == " "
                is_text = len(text) > 0
                return 0 < count <= 6 and is_line_space and is_text
            else:
                return False
    return False


def is_quote(line):
    if not line.startswith(">"):
        return False
    return len(line.strip()) > 1


def is_unordered_list(line):
    check_lines = line.split("\n")
    if len(check_lines) != 1:
        return False
    line = check_lines[0]
    if not line.startswith("- "):
        return False
    text = line[2:]
    return len(text.strip()) > 0


def is_ordered_list(line):
    check_lines = line.split("\n")
    if len(check_lines) != 1:
        return False
    line = check_lines[0]
    count = 0
    for char in line:
        if char.isdigit():
            count += 1
        else:
            break
    if len(line) <= count:
        return False
    if count == 0 or line[count] != ".":
        return False
    if not len(line) > count + 2:
        return False
    line_space = line[count + 1]
    text = line[count + 2:]
    if line_space != " ":
        return False
    return len(text.strip()) != 0


def get_ordered_list_number(line):
    count = 0
    for char in line:
        if char.isdigit():
            count += 1
        else:
            break
    digit = int(line[:count])
    return digit