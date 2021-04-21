import sys, os

name = None
path = None
abs = None
some_directory = (sys.argv[1] if len(sys.argv) > 1 else ".")

i = 2
while i < len(sys.argv):
    x = sys.argv[i]
    if x == "-name":
        name = re.compile(sys.argv[i + 1])
        i += 1

    i += 1;


def iteracja(directory):
    ls = os.listdir(directory)
    for j in ls:
        j = os.path.join(directory, j)
        print(j)
    if os.path.isdir(j):
        iteracja(j)


iteracja(some_directory)
