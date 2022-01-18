import os
import sys

if len(sys.argv) == 1:
    root = '/tmp'
else:
    root = sys.argv[1]

for dir_name, sub_dirs, files in os.walk(root):
    print(dir_name)
    # make the subdirectory names stand out with /.
    sub_dirs = [n + '/' for n in sub_dirs]
    # mix the dir contents together.
    contents = sub_dirs + files
    contents.sort()

    # show the contents.
    for c in contents:
        print(f" {c}")
    print()