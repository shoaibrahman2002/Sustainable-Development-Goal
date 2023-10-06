import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv('./data/cleaned_data.csv')

desc = {
    "poverty": "Percentage of population living below the national poverty line",
    "malnutrition": "Percentage of children under five years who are underweight",
    "literacy": "Percentage of persons (15 years and above) who are literate",
    "drinking water": "Percentage of rural population having improved source of drinking water",
    "electricity": "Percentage of households electrified ",
    "unemployment": "Unemployment rate (%) (15-59 years)",
}

parameters = ["poverty",
              "malnutrition",
              "literacy",
              "drinking water",
              "electricity",
              "unemployment"]


for i in range(1, 7):
    print(i, parameters[i-1])

n = int(input('Select Parameter : '))

parameter = parameters[n-1]

x = list()
y = list()

for i in range(37):
    val = df.loc[i, parameter]
    if(val != 'Null'):
        x.append(df.loc[i, 'States_UT'])
        y.append(round(float(df.loc[i, parameter]), 2))


india = round(float(df.loc[37, parameter]), 2)
target = round(float(df.loc[38, parameter]), 2)

fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=x,
        y=y,
        marker=dict(color=y,
                    colorscale='viridis', showscale=True)
    )
)

fig.add_hline(y=target, line_color="red", annotation_text="Target",
              annotation_position="bottom right")
fig.add_hline(y=india, line_color="blue", annotation_text="India Average",
              annotation_position="bottom right")

fig.update_layout(
    go.Layout(
        title=desc[parameter],
        xaxis=dict(
            title='states/UT'
        ),
        yaxis=dict(
            title='value(in %)',
        )
    )
)

fig.write_html("html/file3.html", auto_open=True)
