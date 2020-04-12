import json
from datetime import datetime
checkinData = [json.loads(line) for line in open('tempeCheckin.json', 'r')]

data = [{}]
# 0 - Monday,. 6 - Sunday
count = {0:{},1:{},2:{},3:{},4:{},5:{},6:{}}
for i in range(7):
    for j in range(24):
        count[i][j] = 0

for i in checkinData:
    values = i["date"]
    i['checkin'] = count.copy()
    for j in values:
        dt = datetime.strptime(j,"%Y-%m-%d %H:%M:%S")
        i['checkin'][dt.weekday()][dt.hour] += 1


with open('tempeBusinessSubset.json', 'w') as my_file:
    json.dump(reducedData, my_file)