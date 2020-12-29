#chapter 20 - Instant Markup
#github code: https://github.com/Apress/beginning-python-3ed/tree/master/Chapter20

import os, sys, re
from util import *

#clear the console
os.system('clear')

#   to write (or read) to a file and print to a file we have to specify the following
#   python simple_markup.py > data/text_output.html
#   python simple_markup.py < data/text_input.txt
#   theFile = open(sys.stdin)
theFile = open('./data/text_input.txt', 'r')

#print to a file instaed of console
f = open('./data/text_output.html', 'w')
sys.stdout = f

#add html to the beginning of the otput file
print('<html><head><title>HTML conversion by GeirOwe</title><body>')

#find the blocks in the file
title = True
for block in blocks(theFile):
    #substitute any text within * ......* with italics and remove the *'s
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')

#add html to the end of the otput file
print('</body></html>')

#print a done message back to console
sys.stdout = sys.__stdout__
print(' ... all good')
print()