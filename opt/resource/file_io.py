import os

def write_to_file(filepath, name):
    with open(filepath, "w+") as file:
        file.write(name)

def read(filepath, filename):
    return open(os.path.join(filepath, filename)).read()
