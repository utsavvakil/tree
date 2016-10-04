#!/usr/bin/env python3
import subprocess
import sys
import os

indent = "|   "
indent_done = "    "
child_branch = "|-- "
child_branch_done = "`-- "
count_dir = 0
count_files = 0

def print_tree(dir_path, offset):
    global count_dir
    global count_files
    all_children = [cont for cont in os.listdir(dir_path) if not cont.startswith('.')]
    children = sorted(all_children, key=lambda s: s.strip('_').lower())
    i = 0
    end_flag = 0
    for child in children:
        if(i < len(children) - 1):
            print(offset + child_branch + str(child))
        else:
            end_flag = 1
            print(offset + child_branch_done + str(child))

        if(os.path.isdir(os.path.join(dir_path, child))):
            count_dir += 1
            if(end_flag == 1):
                print_tree(os.path.join(dir_path, child), offset + indent_done)
            else:
                print_tree(os.path.join(dir_path, child), offset + indent)
        elif(os.path.isfile(os.path.join(dir_path, child))):
            count_files += 1
        i += 1
if __name__ == '__main__':
    dir_path = "."
    count_dir = 0
    count_files = 0
    if(len(sys.argv) == 2):
        dir_path = sys.argv[1]
    if(len(sys.argv) > 2):
        print("Invalid data")
        sys.exit()
    print(dir_path)
    print_tree(dir_path, "") 
    print()
    final_str = str(count_dir) + " directories, " + str(count_files) + " files"
    print(final_str)
