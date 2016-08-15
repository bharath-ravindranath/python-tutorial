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

# +++your code here+++
# Write functions and modify main() to call them
def getSpecialFiles(directory):
  returnList = []
  try:
    files = os.listdir(directory)
    for file in files:
      if re.search(r'__\w+__', file):
        returnList.append(os.path.abspath(os.path.join(directory, file)))
  except OSError as e:
    sys.stderr.write("OS Error: (" + str(e.errno) + ") "+ directory +\
     ": " + e.strerror + "\n")
  return returnList

def copySpecialFiles(todir, files):
  if not os.path.exists(todir):
    os.mkdir(todir)

  for file in files:
    shutil.copy(file, todir)
  return

def zipSpecialFiles(tozip, files):
  cmd = "zip -j " + tozip + " " + " ".join(files)
  if commands.getstatusoutput(cmd)[0]:
    print "Zip failed!"
  return

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
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  sFiles = []
  for directory in args:
    sFiles.extend(getSpecialFiles(directory))

  if todir and sFiles:
    copySpecialFiles(todir, sFiles)

  elif tozip and sFiles:
    zipSpecialFiles(tozip, sFiles)

  elif sFiles:
    print '\n'.join(sFiles)
  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
