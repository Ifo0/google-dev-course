#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

def get_paths(dir):

    filenames = os.listdir(dir)
    f = ", ".join(filenames)
    special_filenames = re.findall(r'\w*__\w*__.\w*', f)
    paths = []
    abs_path = []
    for item in special_filenames:
        paths.append(os.path.join(dir, item))
    for path in paths:
        abs_path.append(os.path.abspath(path))
    return abs_path

def copy_to(file_paths, to_dir):
    if not os.path.exists(to_dir):
        os.mkdir(destination)
    for path in file_paths:
        # fname = os.path.basename(path)
        # shutil.copy(path, os.path.join(to_dir, fname))
        shutil.copy(path, to_dir)

def zip_to(file_paths, zipname):
    cmd = 'zip -j ' + zipname + " " + " ".join(file_paths)
    print("About to run %s, do you want to continue (y/n) ?" %(cmd))
    user_input = raw_input()
    if user_input == 'y':
        (status, output) = commands.getstatusoutput(cmd)
        if status:
            sys.stderr.write(output)
            sys.exit(status)
        else:
            return output
    elif user_input == 'n':
        sys.exit(0)
    else:
        print("Invalid argument provided. Available: y/n")



# +++your code here+++
# Write functions and modify main() to call them



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    to_dir = args[1]
    file_paths = get_paths(args[-1])
    copy_to(file_paths, to_dir)

    # test = copy_to(file_paths, to_dir)
    # print(test)

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    file_paths = get_paths(args[-1])
    print(args)
    zip_to(file_paths, tozip)



  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)



  # +++your code here+++
  # Call your functions



    # if todir:
    #     test = copy_to(file_paths, to_dir)
    #     print(test)
    # else:
    #     print('\n')
    #     print('\n'.join(files))
    #     print('\n')


if __name__ == "__main__":
  main()
