from matplotlib import pyplot as plt
import pandas as pd
import us as us
df_init = pd.read_csv('usgs_earthquakes_2014.csv', index_col=11)
df_init['time'] = pd.to_datetime(df_init.time, format='%Y-%m-%d')
df_init['updated'] = pd.to_datetime(df_init.updated, format='%Y-%m-%d')
df = []
df = df_init
df['country'] = df['place'].str.split(", ").str.get(1)

states = us.STATES
stateList = []
for state in states:
    stateList.append(str(state).upper()) 


def state_check(value):
    value = str(value)
    for state in stateList:
        if value.upper().replace(' ','') == state.replace(' ',''):
            result = True
            break
        else:
            result = False
    return result

df_dropna = df.dropna(subset=['country'])
df_dropna['Is country USA?'] = df_dropna['country'].apply(lambda USA: state_check(USA))
df_dropna['Is country USA?'].fillna(value = False)
df_dropna.reindex(df_dropna.columns, axis="columns")

def state(row):
    if row['Is country USA?'] == True:
        return (row['country'])
    else:
        return ''
df_dropna['State'] = df_dropna.apply(state, axis=1)

def country(row):
    if row['Is country USA?'] == True:
        return 'USA'
    else:
        return row['country']
df_dropna['country'] = df_dropna.apply(country, axis=1)

df_high_mag = df_dropna[df_dropna.mag >= 4]

plt.scatter(df_high_mag.latitude,df_high_mag.longitude,c = df_high_mag.mag)
cbar = plt.colorbar()
cbar.set_label('Magnitude')
plt.title('Magnitude of earthquakes')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.savefig('plot1.jpg')

plt.scatter(df_high_mag.latitude,df_high_mag.longitude,c=df_high_mag.depth)
cbar = plt.colorbar()
cbar.set_label('Depth')
plt.title('Depth of earthquakes')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.savefig('plot2.jpg')