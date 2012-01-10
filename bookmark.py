#! /usr/bin/python


"""
this executable looks at $0
to determine which of 2 soft-linked names it is called as:

use "bookmark" to add a bookmark:

    if one arg, take it as a path and bookmark that
    if zero args, bookmark the pwd

use "bookmark_subtract" to

    search for its one arg and erase it from the bookmarks list

the bookmark list is stored as
/var/
"""


import sys # sys.argv
import os # os.system
import subprocess # .call and .check_output


# Constants. abspath is short for abspath to a file
bookmark_absfile = '/Users/jon/Dropbox/git/bookmark/bookmarks.txt'


###
# Action Jackson

pathed_action = sys.argv[0]
action = os.path.basename(pathed_action)

assert action in ['bookmark', 'bookmark_subtract']


###
# TODO put this class on the modules path

class StringListOutOfBoundsNone():
    
    string_list = None
    
    def __init__(self, string_list):
        """
        e.g. string_list can be sys.argv
        """

        self.string_list = string_list
    # end init

    # [] getter
    def __getitem__(self, i):
        """
        sheer awesomeness below:
        """
        
        # TODO test
        fails = [
                not isinstance(i, int),
                i < 0,
                i >= len(string_list)]

        for fail in fails:
            if fail == true:
                return None

        return string_list[i]
    # BABOOM! Some of my favorite code there :)

# end class


###




raise NotImplementedError



if true:
    print 'hi'
relpath_to_bookmark = sys.argv[1]

file_to_bookmark = os.path.abspath()
