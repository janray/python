#!/usr/bin/python

# makefolder.py
# script by Jan Ray C. Rulida
# December 17, 2014


'''
   This is a script to create several folders from a list.
   The list must contain the intended names of the folders separated by
   a new line. This is useful when you want to batch create folders for a list 
   of students. This is a quick and dirty solution so feel free to modify this
   and improve it.
'''

import os

with open("list.txt") as fileList:
    for line in fileList:
        if not os.path.exists("./" + line[:-1]):
            os.makedirs("./" + line[:-1])
        else:
            print "Folder " + line[:-1] + " already exists."

print "Done creating folders."


fileList.close()
