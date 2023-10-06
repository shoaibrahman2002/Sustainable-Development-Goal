from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import r2_score

df = pd.read_csv('./data/sustainable_goals.csv')


regressor = LinearRegression()


state = df.loc[df['state'] == "Uttar Pradesh"]

years = ['2018', '2019', '2020']

x = list()
y = list()

for year in years:
    x.append(int(year[-2]+year[-1]))
    val = int(state[year])
    if(val > 100):
        y.append(100)
    else:
        y.append(val)

x = np.array(x).reshape(-1, 1)

regressor.fit(x, y)

y_predicted = regressor.predict(x)
accuracy = round(r2_score(y, y_predicted)*100, 2)

plt.title(f'Linear Regressor: Accuracy= {accuracy} %')
plt.xticks(np.arange(18, 24))
plt.xlabel('Year')
plt.ylabel('Composite score')
plt.scatter(x, y, color='red', label='actual')
plt.scatter(x, y_predicted, color='blue', label='predicted')

x_future = [[21], [22], [23]]
y_future = regressor.predict(x_future)

plt.scatter(x_future, y_future, color='orange', label='future')
plt.legend()
plt.show()
