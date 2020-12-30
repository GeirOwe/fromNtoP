#!/usr/bin/python
#project 7 - a bulletin board

print('Content-type: text/html\n')
import cgitb; cgitb.enable()

import os, sys
import sqlite3
from sqlite3 import Error

#start function - create a table first time
def create_table(curs):
    curs.execute('''
    CREATE TABLE messages (
        id          integer primary key autoincrement,
        subject     TEXT NOT NULL,
        sender      TEXT NOT NULL,
        reply_to    int,
        text        TEXT NOT NULL
    )
    ''')
#end create_table function

#start function 
def conv_list_to_dict(rowList):
    rowDict = []
    for row in rowList:
        #combine key value pair
        rowLabels = ['id', 'subject', 'sender', 'reply_to', 'text']
        aDict = dict(zip(rowLabels, row))
        
        #add this new dict to the list
        rowDict.append(aDict)
    return rowDict
#end function

# ----- START OF PROGRAMME ------------
#clear the console and start the programme
os.system('clear')
print('knock knock ...')
print()

#print to a file instead of console
f = open('./data/text_output.html', 'w')
sys.stdout = f

#connect to the database and create the cursor
conn = sqlite3.connect('./database/bulletin.db')
curs = conn.cursor()

#drop table if needed
#drop_table(curs)
#create a table first time
#create_table(curs)
#conn.commit()

#prepare html
print("""
<html>
  <head>
    <title>The GeirOwe Bulletin Board</title>
  </head>
  <body>
    <h1>The GeirOwe Bulletin Board</h1>
    """)

#read all messages
curs.execute('SELECT * FROM messages')
rowList = curs.fetchall()

#in the code below the rows must be of typ dict, 
#so the list must be have all rows as dict
rows = conv_list_to_dict(rowList)

toplevel = []
children = {}
#parse all messages
for row in rows:
    parent_id = row['reply_to']
    if parent_id is None:
        toplevel.append(row)
    else:
        children.setdefault(parent_id, []).append(row)
    def format(row):
        print(row['subject'])
        try: kids = children[row['id']]
        except KeyError: pass
        else:
            print('<blockquote>')
            for kid in kids:
                format(kid)
            print('</blockquote>')

    print('<p>')

    for row in toplevel:
        format(row)

    print("""
        </p>
    </body>
    </html>
    """)