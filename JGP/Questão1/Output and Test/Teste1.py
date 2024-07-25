##Author : Pedro Arthur Santos Gama

import requests
import json
import csv
from datetime import datetime


headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": ['CUSR0000SA0','CUSR0000SA0L1E','CUSR0000SETB01'],"startyear":"2019", "endyear":"2024"})
p = requests.post('https://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)

with open('DATA5.csv','w',newline='') as csvfile:
    campos_head =["date","Year","Month","series 1", "series 2", "series 3"]
    writer = csv.DictWriter(csvfile,fieldnames=campos_head)
    writer.writeheader()

    results = json_data['Results']['series']
    for i in range(len(results[0]['data'])):
        Year = results[0]['data'][i]['year']
        Month = results[0]['data'][i]['periodName']
        datetime_str = f'{Month}/01/{Year}'
        datetime_obj = datetime.strptime(datetime_str, '%B/%d/%Y')
        new_datetime = datetime_obj.strftime('%m/1/%Y')
        firstValue = results[0]['data'][i]['value']
        secondValue = results[1]['data'][i]['value']
        thirdValue = results[2]['data'][i]['value']

        writer.writerow({'date': f'{new_datetime}','Year':f'{Year}','Month':f'{Month}','series 1':f'{firstValue}','series 2':f'{secondValue}','series 3':f'{thirdValue}'})

   
