import pandas as pd
import numpy as np
import plotly.graph_objs as go
df = pd.read_csv('./data/cleaned_data.csv')


parameters = ["poverty",
              "malnutrition",
              "literacy",
              "drinking water",
              "electricity",
              "unemployment"]


for i in range(1, 7):
    print(i, parameters[i-1])

fig = go.Figure()

n = 1
while(n <= 6):
    parameter = parameters[n-1]
    values = df[parameter]

    y = list()

    for val in values:
        if(val == 'Null'):
            continue
        else:
            y.append(round(float(val), 2))

    Q1 = np.quantile(y, 0.25)
    Q3 = np.quantile(y, 0.75)
    IQR = Q3-Q1

    y_filtered = list()
    for x in y:
        if(x >= Q1-1.5*IQR and x <= Q3+1.5*IQR):
            y_filtered.append(x)

    fig.add_trace(go.Box(y=y_filtered, name=parameter))

    n += 1

fig.update_layout(
    go.Layout(
        title="Box Plot",
        xaxis=dict(
            title='parameters'
        ),
        yaxis=dict(
            title='value(in %)',
        )
    )
)

fig.write_html("html/file4.html", auto_open=True)
