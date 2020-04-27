import csv, json, sys
from datetime import datetime
import operator
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import csv
import plotly

# business_id = bhosqo-Q1xp67iLqrd1Rbw

with open("tempeReview.json", "r", encoding="utf-8") as jsonFile:
    data2 = json.load(jsonFile)
    data=[]
    r1=r2=r3=r4=r5=0
    rest='bhosqo-Q1xp67iLqrd1Rbw'
    for i in range(len(data2)):
        if(data2[i]['business_id']==rest):
            data.append(data2[i])
            if(data2[i]['stars']==1.0):
                r1+=1
            if(data2[i]['stars']==2.0):
                r2+=1
            if(data2[i]['stars']==3.0):
                r3+=1
            if(data2[i]['stars']==4.0):
                r4+=1
            if(data2[i]['stars']==5.0):
                r5+=1
    # print(type(data))
    # print(r1,r2,r3,r4,r5)
    # print(len(data))
    jsonFile.close()

fileOutput = 'example.csv'
# inputFile = open(fileInput, encoding="utf-8") #open json file
outputFile = open(fileOutput, 'w',newline='') #load csv file
# data = json.load(inputFile) #load json content
data = sorted(data, key=operator.itemgetter('date'))
# inputFile.close() #close the input file
output = csv.writer(outputFile) #create a csv.write
output.writerow(data[0].keys())  # header row
for row in data:
    output.writerow(row.values()) #values row
