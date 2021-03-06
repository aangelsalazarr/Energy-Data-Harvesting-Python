import pandas as pd
from pandas_datareader import wb
import matplotlib.pyplot as plt
from functools import reduce
import wbdata

# want to grab electricity access data
electricity_access = "EG.ELC.ACCS.ZS"
renewable_electricity_excluding_hydro = "EG.ELC.RNWX.KH"
renewable_energy_consumption = "EG.FEC.RNEW.ZS"  # % of total final energy consumption

# our initial parameters
countries = ["CHN"]
year_start = 2000
year_end = 2018

# creating a dataframe on electricity access
df1 = wb.download(indicator=electricity_access, country=countries, start=2010,
                  end=2018)
# print("electricity access data")
# print(df1, "\n")

# creating a dataframe on renewable electricity excluding hydro
df2 = wb.download(indicator=renewable_electricity_excluding_hydro, country=countries,
                  start=2010, end=2018)
# print("Renewable Electricity")
# print(df2, "\n")

# creating a dataframe on renewable energy consumption (%)
df3 = pd.DataFrame(data=wb.download(indicator=renewable_energy_consumption, country=countries,
                                    start=1990, end=2018))
df3.reset_index(inplace=True)
df3.columns = ['country', 'year', 'value']
df3['year'] = pd.to_datetime(df3['year'])
df3 = df3.sort_values(by='year')

print("Renewable electricity consumption (%)")
print(df3, "\n")

# putting all dataframes in to a list
data_frames = [df1, df2, df3]

# adding titles and axis names
df3.plot(x='year', y='value')
plt.title('China, Renewable Energy Consumption (% of total final energy consumption)')
plt.ylabel('%')
plt.xlabel('Date')

# plotting renewable energy consumption
plt.show()


# creating code to take any request and set up a dataframe from the data
def retrieve_wb_data(wb_indicator):
    """"
    purpose is to take in an indicator value and create a dataframe
    """
    indicator_search = wb.download(indicator=wb_indicator, country=countries,
                                   start=year_start, end=year_end)

    # create a pandas df from the above input
    df=pd.DataFrame(data=indicator_search)
    df.reset_index(inplace=True)
    df.columns=['country', 'year', 'value']
    df['year']=pd.to_datetime(df['year'])
    df=df.sort_values(by='year')
    return df

print(retrieve_wb_data(electricity_access))