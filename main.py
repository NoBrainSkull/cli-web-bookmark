import sys
import sqlite3
from subprocess import call
from bookmark import Bookmark

NEW_TAB_COMMAND = "google-chrome"

def run():
    """
    Main
    """
    if len(sys.argv) > 2 and sys.argv[1] == '-r':
        Bookmark.select(sys.argv[2]).delete()
    elif len(sys.argv) > 2 and Bookmark.select(sys.argv[1]) is None:
        Bookmark(sys.argv[1], sys.argv[2]).persist()
    else:
        bookmark = Bookmark.select(sys.argv[1])
        if bookmark is not None:
            call([NEW_TAB_COMMAND, bookmark.link])
        else:
            print('No bookmark ' + sys.argv[1])
run()
