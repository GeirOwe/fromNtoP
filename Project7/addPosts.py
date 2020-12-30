#a utility program to add post since we have no GUI yet

import sqlite3
from sqlite3 import Error
import os

# ----- START OF PROGRAMME ------------
#clear the console and start the programme
os.system('clear')
print('inserting some posts since we lack a GUI for that at the moment ...')
print()

#connect to the database and create the cursor
conn = sqlite3.connect('./database/bulletin.db')
curs = conn.cursor()

#get a Post from keyboard
reply_to = input('reply to(null hvis dette ikke er respons til en annen melding): ')
subject = input('subject: ')
sender = input('sender: ')
text = input('text: ')
if not (sender and subject and text):
    print('Please supply sender, subject, and text')
    sys.exit()

#create the sql tring
if reply_to:
    query = """
    INSERT INTO messages(reply_to, sender, subject, text)
    VALUES({}, '{}', '{}', '{}')""".format(reply_to, sender, subject, text)
else:
    query = """
    INSERT INTO messages(sender, subject, text)
    VALUES('{}', '{}', '{}')""".format(sender, subject, text)

# execute sql t add the post to the database, and commit change
curs.execute(query)
conn.commit()