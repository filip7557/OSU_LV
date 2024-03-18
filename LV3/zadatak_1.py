import pandas as pd

data = pd.read_csv("OSU_LV\LV3\data_C02_emission.csv")

#a
print("Broj mjerenja:", len(data))
print(data.info())
print(data.dropna())
print(data.drop_duplicates())

data["Make"] = data["Make"].astype("category")
data["Model"] = data["Model"].astype("category")
data["Vehicle Class"] = data["Vehicle Class"].astype("category")
data["Transmission"] = data["Transmission"].astype("category")
data["Fuel Type"] = data["Fuel Type"].astype("category")

print(data.info())

#b
df = data.sort_values(by="Fuel Consumption City (L/100km)", ascending=False)
print(df[["Make", "Model", "Fuel Consumption City (L/100km)"]].head(3))
print(df[["Make", "Model", "Fuel Consumption City (L/100km)"]].tail(3))

#c
df = data[(data['Engine Size (L)'] >= 2.5) & (data['Engine Size (L)'] <= 3.5)]
print("Broj vozila s velicinom motora izmedu 2.5 i 3.5L:", len(df))
print("Prosjecna CO2 emisija za ova vozila:", df["CO2 Emissions (g/km)"].mean())

#d
df = data[data['Make'] == 'Audi']
print(df)
print("Broj Audi vozila:", len(df))
df = df[df['Cylinders'] == 4]
print("Prosjecna emisija CO2 Audi vozila s 4 cilindra:", df['CO2 Emissions (g/km)'].mean())

#e
df = data.groupby('Cylinders')
print(df.agg('count')[['Model']])
print(df['CO2 Emissions (g/km)'].mean())

#f
df = data.groupby('Fuel Type')
print(df['Fuel Consumption City (L/100km)'].mean())
print(df['Fuel Consumption City (L/100km)'].median())

#g
df = data[(data['Fuel Type'] == 'D') & (data['Cylinders'] == 4)]
print(df.sort_values(by='Fuel Consumption City (L/100km)', ascending=False).head(1)[["Make", "Model", "Fuel Consumption City (L/100km)"]])

#h
df = data[(data["Transmission"] == 'M5') | (data["Transmission"] == 'M6') | (data["Transmission"] == 'M7')]
print("Broj vozila s rucnim mjenjacem:", len(df))

#i
print(data.corr(numeric_only=True))