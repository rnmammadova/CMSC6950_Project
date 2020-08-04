import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import country_converter as coco

df = pd.read_csv('WHO-COVID-19-global-data.csv')
df['Date_reported'] = pd.to_datetime(df.Date_reported, format='%Y-%m-%d')
df.columns = df.columns.str.strip()
df = df[df.Country != 'Other']

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

df_last_day = df[df.Date_reported == max(df['Date_reported'])]
top_cases = df_last_day.sort_values('Cumulative_cases',ascending = False).head(10)

top_deaths = df_last_day.sort_values('Cumulative_deaths',ascending = False).head(10)

df_last_day['death_rate']=df_last_day.Cumulative_deaths/df_last_day.Cumulative_cases
top_death_rate = df_last_day.sort_values('death_rate',ascending = False).head(10)
top_death_rate = top_death_rate.reset_index()

country = list(top_death_rate.ISO3) 
cases = top_death_rate['Cumulative_cases'] 
deaths = top_death_rate['Cumulative_deaths']
rates=top_death_rate['death_rate']
r = range(len(country))

width_chart = 15

fig  = plt.figure(figsize=(width_chart,7))
ax = fig.add_subplot(111)
ax2 = ax.twinx()

x = np.arange(len(country))  # the label locations
width = width_chart/32 #.55  # the width of the bars

rects1 = ax.bar(x - width/2, cases, width, label='cases')
rects2 = ax.bar(x + width/2, deaths, width, label='deaths')
line1 = ax2.plot(x,rates, color='g', linewidth=10)

plt.title('Details of top 10 countries with highest death rate', size=20)
plt.xticks(r, country)
ax.set_ylabel("Number of cases/deaths", size=15)
ax2.set_ylabel("Number of rates", size=15)
ax.set_xlabel("Country", size=15)
ax.set_yscale("log")

plt.xlim(-width,len(country)-width/2)

ax.legend(['Deaths','Cases'], fontsize=10, loc='upper left',bbox_to_anchor=(0,.8))
ax2.legend(['Rates'], fontsize=10, bbox_to_anchor=(1,1))
for i,j in enumerate(cases):
    ax.text(i-width/2, j, j, horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':10})

for i,j in enumerate(deaths):
    ax.text(i+width/2, j, j, horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':10})

for i,j in enumerate(rates):
    ax2.text(i, j, round(j,4), horizontalalignment='center', verticalalignment='top', fontdict={'color':'black', 'fontweight':500, 'size':15})

    
fig.tight_layout()

plt.savefig('plot1.jpg')


x1=top_cases['ISO3']
x2=top_deaths['ISO3']
y1=top_cases['Cumulative_cases']
y2=top_deaths['Cumulative_deaths']

f = plt.figure(figsize=(12,9))

plt.subplot(2,1,1)
pop = plt.bar(x1, y1)
plt.ylabel('Total number of cases')
plt.xticks(x1, rotation='horizontal')

for i,j in enumerate(y1):
    plt.text(i, j, float(j), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':9})
plt.subplot(2,1,2)
gdp =plt.bar(x2, y2)
plt.ylabel('Total number of deaths')
#plt.yscale('log')
plt.xticks(x2, rotation='horizontal')
for i,j in enumerate(y2):
    plt.text(i, j, float(j), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':9})

plt.savefig('plot2.jpg')