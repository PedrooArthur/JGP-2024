#Author : Pedro Arthur Santos Gama

import plotly.express as px
import pandas as pd

df = pd.read_csv('ALLDATA.csv') ##CSV made in Question1

lista_values = [ ((df['series 2'][i]- df['series 2'][i -12])/df['series 2'][i-12])*100 for i in range(12, len(df['date']))] # Picking the YoY since 2020.
                                                                                                                            # Because the question said to use the data since 2019 we can only calculate the YoY since 2020

lista_datetime = [df['date'][i] for i in range(12, len(df['date']))]

lista_prices = [df['series 2'][i] for i in range(12,len(df['series 2']))]

df1 = pd.DataFrame({'name': 'prices' , 'y': lista_prices , 'x' : lista_datetime})
df2 = pd.DataFrame({'name': 'variation' ,'y': lista_values , 'x': lista_datetime})
df = pd.concat([df1,df2])
fig = px.line(df, x = 'x', y='y' , color = 'name' , markers=True)
fig.show()
