
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

filter = raw_input('Enter Mfg >')

# filter = 'Audi'

con = lite.connect('test.db')

with con:

    # filter = 'Audi'

    cur = con.cursor()
    cur.execute("SELECT * FROM Cars where name = ? ", (filter,))

    rows = cur.fetchall()

    for row in rows:
        print row
