#this utility file generates a text block 
def lines(file):
    for line in file: yield line
    yield '\n'

#looks for a block of text in a file that belong together
#this is added to a specific block and all whitespaces and EOL are stripped away
def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []