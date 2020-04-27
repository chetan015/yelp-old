import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import csv
import plotly

df = pd.read_csv('example.csv')
# print(len(df['stars']))
fig = px.line(df, x='date', y='stars',title='Rating Time Series for Restaurant X')

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
# fig.show()
# print(df['stars'][0])
r1=r2=r3=r4=r5=0
for i in range(len(df)):
    if(df['stars'][i]==1.0):
        r1+=1
    if(df['stars'][i]==2.0):
        r2+=1
    if(df['stars'][i]==3.0):
        r3+=1
    if(df['stars'][i]==4.0):
        r4+=1
    if(df['stars'][i]==5.0):
        r5+=1
df2 = pd.DataFrame(dict(
    rall=[r1,r2,r3,r4,r5],
    theta=['1 star','2 star','3 star','4 star','5 star']))
fig2 = px.line_polar(df2, r='rall', theta='theta', line_close=True)
fig2.show()
