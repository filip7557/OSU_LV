import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import sklearn.linear_model as lm
import numpy as np

data = pd.read_csv("LV4\data_C02_emission.csv")

ohe = OneHotEncoder()
X_encoded = ohe.fit_transform(data[['Fuel Type']]).toarray()
data['Fuel Type'] = X_encoded

X = data[['Engine Size (L)', 'Cylinders', 'Fuel Consumption City (L/100km)', 'Fuel Consumption Hwy (L/100km)', 'Fuel Consumption Comb (L/100km)', 'Fuel Consumption Comb (mpg)', 'Fuel Type']]


y = data[['CO2 Emissions (g/km)']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

linearModel = lm.LinearRegression()
linearModel.fit(X_train, y_train)

y_test_p = linearModel.predict(X_test)

max_pogreska = 0
max_pogreska_loc = 0

y_true = np.array(y_test)

for i in range(len(y_test)):
    pogreska = abs(y_true[i] - y_test_p[i])
    if(pogreska > max_pogreska):
        max_pogreska = pogreska
        max_pogreska_loc = i

print("Najveca pogreska(g/km):", max_pogreska, data.iloc[max_pogreska_loc][['Make']], data.iloc[max_pogreska_loc][['Model']])