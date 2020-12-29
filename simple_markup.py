#chapter 20 - Instant Markup
#github code: https://github.com/Apress/beginning-python-3ed/tree/master/Chapter20

import os, sys, re
from util import *

#start function
def main_html(blockNo):
    if blockNo == 1:
        print('<html><head><title>HTML conversion by GeirOwe</title><body>')
    else:
        print('</body></html>')
#end function

#start function
def parse_block(aBlock):
    #substitute any text within * ......* with italics and remove the *'s
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', aBlock)
    return block
#end function

#start function
def define_block_type(theBlock, blockNo):
    if blockNo == 1:
        block_type = 'mainHeading'
    else:
        if ('\n' in theBlock) or (':' in theBlock) or ('-' in theBlock):
            if theBlock.startswith('-'):
                block_type = 'listitem'
            else:
                block_type = 'avsnitt'
        else:
            block_type = 'heading'
    return block_type
#start function

#start function
def apply_html_tags(theBlock, blockNo):
    block_type = define_block_type(theBlock, blockNo)
    if block_type == 'mainHeading':
        print('<h1>')
        print(pBlock)
        print('</h1>')
    else:
        if block_type == 'heading':
            print('<h2>')
            print(pBlock)
            print('</h2>')
        else:
            if block_type == 'avsnitt':
                print('<p>')
                print(pBlock)
                print('</p>')
            else:
                if block_type == 'listitem':
                    print('<ul>')
                    print(pBlock)
                    print('</ul>')
#end function

# ----- START OF PROGRAMME ------------
#clear the console and start the programme
os.system('clear')
print('< the beginning >')

# alternative read statement - start the program as follows:   python simple_markup.py < data/text_input.txt
# the open statement will then be: theFile = open(sys.stdin)
theFile = open('./data/text_input.txt', 'r')

#print to a file instead of console
f = open('./data/text_output.html', 'w')
sys.stdout = f
#keep track of which block
blockNo = 1

#add html to the beginning of the otput file
main_html(blockNo)

#deal with the the blocks in the file
for block in blocks(theFile):
    #parse the block to tidy up text
    pBlock = parse_block(block)

    #add the proper html to the block
    apply_html_tags(pBlock, blockNo)
    blockNo = blockNo + 1

#add html to the end of the output file
main_html(blockNo)

#print a "done message" back to console
sys.stdout = sys.__stdout__
print('< the end >')