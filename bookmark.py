import sqlite3

#Config
BDDPATH = 'db/bookmark'
CONN = sqlite3.connect(BDDPATH)
CLASSCURSOR = CONN.cursor()
CLASSCURSOR.execute('CREATE TABLE IF NOT EXISTS websites (shortname text, link text)')
CONN.commit()

class Bookmark:
    """
    A bookmark object
    """

    def __init__(self, shortname, link):
        self.shortname = shortname
        self.link = link
        self.cursor = CONN.cursor()

    def persist(self):
        """
        Save Bookmark into db
        """
        args = (self.shortname, self.link)
        self.cursor.execute("INSERT INTO websites VALUES (?, ?)", args)
        CONN.commit()

    def delete(self):
        """
        Remove a bookmark from db
        """
        shortname = (self.shortname,)
        self.cursor.execute('DELETE FROM websites WHERE shortname=?', shortname)
        CONN.commit()

    @staticmethod
    def select(shortname):
        """
        Get a bookmark from db
        """
        shortname = (shortname,)
        CLASSCURSOR.execute('SELECT shortname, link FROM websites WHERE shortname=?', shortname)
        row = CLASSCURSOR.fetchone()
        if row is not None:
            return Bookmark(row[0], row[1])
        else:
            return None
