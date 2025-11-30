'''
You have been provided with ‘leeds-central-air-quality.csv’ which is a file containing air quality data for Leeds from the last few years. There are 4 values – particulate matter (25), particulate matter (10), Ozone and Nitrous Oxide which are all different measures of air quality – which are recorded against the date.
Load this file into a suitable data structure.

From this data, create a line plot of the average of the 4 data points against the date.

For example, for the row:
07/09/2024,68,20,25,5

You would plot a point at (68+20+25+5)/4 = 29.5

The X-axis should be the date, the Y-axis should be the average pollution.
'''
# Zariyah Omar 202029002 

import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("leeds-central-air-quality.csv")

data.columns = data.columns.str.strip().str.lower()

print(data.columns)

column_mapping = {
    'pm25': 'pm25',
    'particulate matter (25)': 'pm25',
    'pm10': 'pm10',
    'particulate matter (10)': 'pm10',
    'o3': 'o3',
    'ozone': 'o3',
    'no2': 'no2',
    'nitrous oxide': 'no2',
    'date': 'date'
}

data = data.rename(columns=column_mapping)

pollution_columns = ['pm25', 'pm10', 'o3', 'no2']

data['date'] = pd.to_datetime(data['date'], dayfirst=True)

data['average_pollution'] = data[pollution_columns].mean(axis=1)

plt.figure(figsize=(12,6))
plt.plot(data['date'], data['average_pollution'], marker='o', linestyle='-')
plt.xlabel("Date")
plt.ylabel("Average Pollution")
plt.title("Leeds Air Quality: Average Pollution Over Time - Zariyah Omar")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

