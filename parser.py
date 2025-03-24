import json

def write(to_be_written, file_name="structure.txt"): 
    with(open(file_name, 'w')) as file: 
        file.write(json.dumps(to_be_written))


def read(filename="structure.txt"):
    with(open(filename, 'r')) as file: 
        return json.loads(file.read())

def print_blocks(block_string):
    blocks = block_string.split(' ')
    out = ""
    for i, block in enumerate(blocks, start=0):
        out += f"{block}" + " " + f"{i}" + "  "
    print(out)