#! /usr/bin/python


"""
the bookmarks are a stack
bashrc cd's to the most recent bookmark.

if called with one arg that is not an option, bookmarks that path

valid options:
  '-l' or '--list': cats bookmarks.txt (most recent catted last)
  '-p' or '--pop': says the name of the most recent bookmark, and asks for confirmation to delete it
  '--recentest': says the name of the most recent bookmast
  '--edit': opens bookmarks_file in the user's editor (just uses mac open, but TODO use the VISUAL or EDITOR variables)
"""


import sys # sys.argv
import os # os.system
import subprocess # .call and .check_output


# Constants. abspath is short for abspath to a file
bookmarks_file = '/Users/jon/Dropbox/git/bookmark/bookmarks.txt'


# fns

def b_add(rel_path):
    abs_path = os.path.abspath(rel_path)
    
    # 'a' for append
    with open(bookmarks_file, 'a') as fa:
        fa.write(abs_path + '\n')

def b_list():
    subprocess.call(['cat', bookmarks_file])

def b_confirm_then_pop():

    with open(bookmarks_file, 'r') as fr:
        
        lines = fr.readlines()

    if len(lines) <= 1:
        
        print "can't delete the '~' entry because we need a home directory."
        return


    print "really delete this entry?"
    print lines[-1]

    yn = raw_input('y/n: ')
    if yn == 'y':

        with open(bookmarks_file, 'w') as fw:
            
            for line in lines[:-1]:
                
                fw.write(line) # line includes the \n

        print "deleted!"

# end def

def b_print_recentest():

    with open(bookmarks_file, 'r') as fr:
        
        lines = fr.readlines()
        print lines[-1]

# end def

def b_editor():
    
    subprocess.call(['open', bookmarks_file])

# end def


###
# Action Jackson
#
#  The below code is beeeauuutiful. :)

if len(sys.argv) == 2:
        
    if sys.argv[1] in ['-l', '--list']:
        b_list()

    elif sys.argv[1] in ['-p', '--pop']:
        b_confirm_then_pop()

    elif sys.argv[1] in ['--recentest']:
        b_print_recentest()

    elif sys.argv[1] in ['--edit']:
        b_editor()

    else:
        b_add(sys.argv[1])

elif len(sys.argv) == 1:
    
    # rookie mistake to try to use 'bookmark' to add. The correct usage is 'bookmark .'

    print "warning: did you mean 'bookmark .'?"

# done, woot!

