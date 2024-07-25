##Author : Pedro Arthur Santos Gama

import requests
import json
import csv
from datetime import datetime
##As the Date field originally, as it was formatted in the JGP example PDF, does not exist when we perform the Json Request, 
# given that the report is monthly, we need to convert what we have to the requested format"

headers = {'Content-type': 'application/json'}

data = json.dumps({"seriesid": ['CUSR0000SA0','CUSR0000SA0L1E','CUSR0000SETB01'],"startyear":"1967", "endyear":"1973"})##As the JGP email did not specify the 
                                                                                                                        ##desired time, for request limitation reasons I did the 
                                                                                                                        ## initial data being 2019 and the end 2024, given that we will use
                                                                                                                        #these values ​​in question 2. The value of the id's can be found in
                                                                                                                        ## https://download.bls.gov/pub/time.series/cu/cu.series
                                                                                    

p = requests.post('https://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers)

json_data = json.loads(p.text)

with open('ALLDATA.csv','w',newline='') as csvfile:

    campos_head =["date","series 1", "series 2", "series 3"] 

    writer = csv.DictWriter(csvfile,fieldnames=campos_head)

    writer.writeheader()

    results = json_data['Results']['series']

    aux = len(results[0]['data'])

    for i in range(aux):

        Year = results[0]['data'][aux-i-1]['year']

        Month = results[0]['data'][aux - i -1]['periodName']

        datetime_str = f'{Month}/01/{Year}'

        datetime_obj = datetime.strptime(datetime_str, '%B/%d/%Y') 

        new_datetime = datetime_obj.strftime('%m/1/%Y')##Here we format the datetime to have an output similar to the exemplary format delivered as stated above.
                                                        # To do this, we format it for any standard day. The important thing is not the return day but the CPI value in the month
                                                        ##I just put this day to fit the standard provided as an example by the company JGP.

        firstValue = results[0]['data'][i]['value'] ## firstValue is the variable that stores the values ​​referring to seriesid = CUSR0000SA

        secondValue = results[1]['data'][i]['value']## secondValue is the variable that stores the values ​​referring to seriesid = CUSR0000SA0L1E

        thirdValue = results[2]['data'][i]['value']## thirdValue is the variable that stores the values ​​referring to seriesid = CUSR0000SETB01

        writer.writerow({'date': f'{new_datetime}','series 1':f'{firstValue}','series 2':f'{secondValue}','series 3':f'{thirdValue}'}) ##Series 1 stores the value referring to 'CPI ALL items"
                                                                                                                                        ##Series 2 stores the value referring to 'CPI ALL items less food'
                                                                                                                                        ##Series 3 stores the value related to 'CPI Gasoline (all types)'

   