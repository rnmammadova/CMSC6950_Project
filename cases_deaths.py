import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import country_converter as coco

#Reading the data
df = pd.read_csv('WHO-COVID-19-global-data.csv', parse_dates=['Date_reported'])
df.columns = df.columns.str.strip()
df = df[df.Country != 'Other']

#Data processing with coco
CountryList, ConvertList = [], []
for row in df['Country']:
    if row not in CountryList:
        CountryList.append(row)
        ConvertList.append(coco.convert(names=row, to='ISO3'))       
df_Converted = pd.DataFrame(list(zip(CountryList, ConvertList)), 
               columns =['Country', 'ISO3']) 
def convert(value):
    result = df_Converted[df_Converted['Country'] == value].ISO3.item()
    return result
df['ISO3'] = df['Country'].apply(lambda country: convert(country))

#Defining top 10 cases and top 10 deaths
df_last_day = df[df.Date_reported == max(df['Date_reported'])]
top_cases = df_last_day.sort_values('Cumulative_cases',ascending = False).head(10)
top_deaths = df_last_day.sort_values('Cumulative_deaths',ascending = False).head(10)

#Figure containg 2 subplots:1 for cases and 1 for deaths
x1=top_cases['ISO3']
x2=top_deaths['ISO3']
y1=top_cases['Cumulative_cases']
y2=top_deaths['Cumulative_deaths']
f = plt.figure(figsize=(12,9))
plt.subplot(2,1,1)
pop = plt.bar(x1, y1)
plt.ylabel('Total number of cases')
plt.xlabel('Country')
plt.xticks(x1, rotation='horizontal')
for i,j in enumerate(y1):
    plt.text(i, j, float(j), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':9})
plt.subplot(2,1,2)
gdp =plt.bar(x2, y2)
plt.ylabel('Total number of deaths')
plt.xlabel('Country')
plt.xticks(x2, rotation='horizontal')
for i,j in enumerate(y2):
    plt.text(i, j, float(j), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':9})
plt.savefig('cases_deaths.jpg')



