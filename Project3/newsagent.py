# Project 4 in the beginning python book - from novice to professional

import os
import nntplib
from nntplib import NNTP

#clear the console and start the programme
os.system('clear')
print('wake up geirowe ......')
print()

#Aioe.org hosts a public news server, a USENET site that is intentionally kept open for 
# all IP addresses without requiring any kind of authentication both for reading and for 
# posting. In order to avoid mass abuses, every IP address is authorized to post no more 
# than 40 messages per day.
#server = NNTP('nntp.aioe.org')
#x = server.group('comp.lang.python.announce')[0]
#print(x)

servername = 'nntp.aioe.org'
group = 'comp.lang.python.announce'
server = NNTP(servername)
howmany = 10

resp, count, first, last, name = server.group(group)

start = last - howmany + 1

resp, overviews = server.over((start, last))

for id, over in overviews:
    subject = over['subject']
    resp, info = server.body(id)
    print(subject)
    print('-' * len(subject))
    for line in info.lines:
        print(line.decode('latin1'))
    print()

server.quit()
