import csv, json, sys
from datetime import datetime
import operator
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import csv
import io
import plotly

with open("tempeReview.json", "r", encoding="utf-8") as jsonFile:
    data2 = json.load(jsonFile)
    data=[]
    rest='bhosqo-Q1xp67iLqrd1Rbw'
    for i in range(len(data2)):
        if(data2[i]['business_id']==rest):
            data.append(data2[i])
    jsonFile.close()

fileOutput = 'example.csv'
outputFile = open(fileOutput, 'w',newline='', encoding="utf-8") #load csv file
data = sorted(data, key=operator.itemgetter('date'))
output = csv.writer(outputFile) #create a csv.write
output.writerow(data[0].keys())  # header row
for row in data:
    output.writerow(row.values()) #values row
