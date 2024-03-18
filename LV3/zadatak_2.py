import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("OSU_LV\LV3\data_C02_emission.csv")

#a
plt.figure()
data['CO2 Emissions (g/km)'].plot(kind='hist', bins=20)
plt.show()

#b
df1 = data[data['Fuel Type'] == 'E']
df2 = data[data['Fuel Type'] == 'D']
df3 = data[data['Fuel Type'] == 'Z']
df4 = data[data['Fuel Type'] == 'X']
plt.scatter(df1["Fuel Consumption City (L/100km)"], df1['CO2 Emissions (g/km)'], c='blue', s=0.5)
plt.scatter(df2["Fuel Consumption City (L/100km)"], df2['CO2 Emissions (g/km)'], c='black', s=0.5)
plt.scatter(df3["Fuel Consumption City (L/100km)"], df3['CO2 Emissions (g/km)'], c='green', s=0.5)
plt.scatter(df4["Fuel Consumption City (L/100km)"], df4['CO2 Emissions (g/km)'], c='red', s=0.5)
plt.show()

#c
data.boxplot(column=['Fuel Consumption Hwy (L/100km)'], by='Fuel Type')
plt.show()

#d
df = data.groupby("Fuel Type")
df.agg('count')[['Model']].plot(kind="bar")
plt.show()

#e
df = data.groupby('Cylinders')
df.agg('mean')[['CO2 Emissions (g/km)']].plot(kind="bar")
plt.show()