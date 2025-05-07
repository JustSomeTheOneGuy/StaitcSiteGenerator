

def markdown_to_blocks(markdown):
    # This function should seperate different sections of a markdown document into blocks
    cleaned_blocks = []
    # seperates the text by two new lines
    print(f"input markdown: {repr(markdown)}")
    markdown = markdown.strip()
    raw_blocks = markdown.split("\n\n")
    print(f"raw blocks: {raw_blocks}")
    for block in raw_blocks:
        stripped_block = block.strip()
        print(f"stripped_block: {stripped_block}")
        # skips empty blocks
        if stripped_block:
            if "\n" in stripped_block:
                lines = block.split("\n")
                print(f"lines: {lines}")
                # strip whitespace for each line in lines
                cleaned_lines = [line.strip() for line in lines]
                print(f"cleaned_lines: {cleaned_lines} lenght of cleaned_lines: {len(cleaned_lines)}")
                # join the cleaned_lines with a new line
                cleaned_block = "\n".join(cleaned_lines)
                print(f"cleaned_block: {cleaned_block} length of cleaned_block: {len(cleaned_block)}")
                cleaned_blocks.append(cleaned_block)
            else:
                cleaned_blocks.append(stripped_block)
    print(f"cleaned_blocks after loop: {cleaned_blocks}")
    return cleaned_blocks

    
    
    # cleaned_lines = [line.strip() for line in lines]
