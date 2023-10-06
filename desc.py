import plotly.graph_objects as go

desc = {
    "poverty": "Percentage of population living below the national poverty line",
    "malnutrition": "Percentage of children under five years who are underweight",
    "literacy": "Percentage of persons (15 years and above) who are literate",
    "drinking water": "Percentage of rural population having improved source of drinking water",
    "electricity": "Percentage of households electrified ",
    "unemployment": "Unemployment rate (%) (15-59 years)",
}

values = [list(desc.keys()), list(desc.values())]


fig = go.Figure(data=[go.Table(
    columnorder=[1, 2],
    columnwidth=[80, 400],
    header=dict(
        values=[['<b>Parameter</b>'],
                ['<b>Description</b>']],
        line_color='darkslategray',
        fill_color='royalblue',
        align=['left', 'center'],
        font=dict(color='white', size=12),
        height=40
    ),
    cells=dict(
        values=values,
        line_color='darkslategray',
        fill=dict(color=['paleturquoise', 'white']),
        align=['left', 'center'],
        font_size=12,
        height=30)
)
])


fig.write_html("html/file5.html", auto_open=True)
