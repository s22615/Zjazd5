import os
import sys

directory = "."
one_per_line = False
display_hidden = False
display_more = False
sep = " "
more_format = "{st_size}bytes {st_mode} {file_name}"

i=1
while i<len(sys.argv):
    x = sys.argv[i]
    if x == "-1":
        sep = "\n"
    elif x == "-a":
        display_hidden = True
    elif x == "-l":
        sep = "\n"
        display_more = True
    elif x == "-f":
        more_format = sys.argv[i+1]
        i += 1
    else:
        directory = x
    i += 1

ls = os.listdir(directory)

if not display_hidden:
    ls1 = []
    for x in ls:
        if x[0] == ".":
            continue
        else:
            ls1.append(x)
    ls = ls1

if display_more:
    ls1 = []
    for x in ls:
        more = os.stat(x)
        ls1.append(more_format.format(st_size = more.st_size,st_mode = oct(more.st_mode),file_name = x))
    ls = ls1
print(sep.join(ls))

