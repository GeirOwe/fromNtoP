# Project 2: paint a pretty picture

# The ReportLab Toolkit (https://www.reportlab.com/) is a library for programatically creating documents 
# in PDF format. It's a robust, flexible, time-proven, industry-strength solution. It's free, open-source 
# software written in Python. It lets you quickly and easily create or automate complex or data-driven documents. 
# The ReportLab Toolkit has evolved over the years in direct response to the real-world reporting needs of large institutions.
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF
import json

#start function
def get_data():
    #the file contaning all data
    with open('./data/flux.json') as f:
        dataJson = json.load(f)
 
    #add the data in the json file to the dataset
    dataSet = []
    for element in dataJson:
        #split time into two columns
        splitX = element['time-tag'].split('-')
        yearX = int(splitX[0])
        monthX = int(splitX[1])

        #add the element-tuple to the list
        dataSet.append(tuple((yearX, monthX , element['predicted_ssn'], element['high_ssn'], element['low_ssn'])))  ## add list of elems at end
    
    return dataSet
#end function

#get the data
data = get_data()

drawing = Drawing(400, 200)

pred = [row[2] for row in data]
high = [row[3] for row in data]
low = [row[4] for row in data]
times = [row[0] + row[1]/12.0 for row in data]

lp = LinePlot()
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = [list(zip(times, pred)),
           list(zip(times, high)),
           list(zip(times, low))]
lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.red
lp.lines[2].strokeColor = colors.green

drawing.add(lp)

drawing.add(String(250, 150, 'Sunspots',
            fontSize=14, fillColor=colors.red))

renderPDF.drawToFile(drawing, 'report2.pdf', 'Sunspots')