import pandas as pd
import plotly.express as px

df = pd.read_csv('./data/cleaned_data.csv')
df.set_index('States_UT', inplace=True)

desc = {
    "poverty": "Percentage of population living below the national poverty line",
    "malnutrition": "Percentage of children under five years who are underweight",
    "literacy": "Percentage of persons (15 years and above) who are literate",
    "drinking water": "Percentage of rural population having improved source of drinking water",
    "electricity": "Percentage of households electrified ",
    "unemployment": "Unemployment rate (%) (15-59 years)",
}

L = ["Andhra Pradesh",
     "Arunachal Pradesh",
     "Assam",
     "Bihar",
     "Chhattisgarh",
     "Goa",
     "Gujarat",
     "Haryana",
     "Himachal Pradesh",
     "Jharkhand",
     "Karnataka",
     "Kerala",
     "Madhya Pradesh",
     "Maharashtra",
     "Manipur",
     "Meghalaya",
     "Mizoram",
     "Nagaland",
     "Odisha",
     "Punjab",
     "Rajasthan",
     "Sikkim",
     "Tamil Nadu",
     "Telangana",
     "Tripura",
     "Uttar Pradesh",
     "Uttarakhand",
     "West Bengal",
     "Andaman and Nicobar Islands",
     "Chandigarh",
     "Dadra and Nagar Haveli",
     "Daman and Diu",
     "Delhi",
     "Jammu and Kashmir",
     "Ladakh",
     "Lakshadweep",
     "Puducherry"]

for i in range(1, len(L)+1):
    print(i, L[i-1])

n = int(input('Select State/UT : '))

name = L[n-1]

x = list()
y = list()

for key in desc:
    val = df.loc[name, key]
    if(val == 'Null'):
        continue
    else:
        y.append(round(float(val), 2))
        x.append(key)

df = pd.DataFrame(dict(
    r=y,
    theta=x))

fig = px.line_polar(df, r='r', theta='theta', line_close=True, title=name)
fig.update_traces(fill='toself')
fig.write_html("html/file2.html", auto_open=True)
