
# This function should seperate different sections of a markdown document into blocks
def markdown_to_blocks(markdown):
    # first strip trailing whitespace from the input markdown
    markdown = markdown.strip()
    # Then split by two newlines
    raw_blocks = markdown.split("\n\n")
    # cycle through each block
    cleaned_blocks = []
    for block in raw_blocks:
        # strip trailing white space for each block
        stripped_block = block.strip()
        # skips empty blocks
        if stripped_block:
            # if there is a newline in the middle of a stripped block
            if "\n" in stripped_block:
                # split the block into lines
                lines = stripped_block.split("\n")
                # strip whitespace for each line in lines
                cleaned_lines = [line.strip() for line in lines]
                # join the cleaned_lines with a new line
                cleaned_block = "\n".join(cleaned_lines)
                # append cleaned_blocks with the cleaned_block
                cleaned_blocks.append(cleaned_block)
            else:
                # if there is no newline in the block, just append to cleaned_blocks
                cleaned_blocks.append(stripped_block)
    return cleaned_blocks

