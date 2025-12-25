import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.read_csv(r"C:\Users\HP\Desktop\Patient.csv")
print(df)
//patient.csv
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\HP\Desktop\Patient.csv")

x = df["Heart_Rate_Category"]   # ✅ correct
y = df["Name"]

plt.xlabel("Heart Rate Category", fontsize=14)
plt.ylabel("Patient Name", fontsize=12)

plt.plot(x, y, color='red')


plt.show()
//heart rate category 

import pandas as pd
import matplotlib.pyplot as plt

# Load file
df = pd.read_csv(r"C:\Users\HP\Desktop\Patient.csv")

# Filter Amit row
amit_row = df[df["Name"] == "Amit"]
print(amit_row)
# amit patient details 

import pandas as pd

# Read Excel file
df = pd.read_csv(r"C:\Users\HP\Desktop\Patient.csv")
# Loop through Name and Cholesterol columns
for i in range(len(df)):
    name = df.loc[i, "Name"]
    cholesterol = df.loc[i, "Cholesterol_mg_per_dL"]

    if cholesterol < 200:
        status = "Normal"
    elif cholesterol < 240:
        status = "Borderline High"
    else:
        status = "High"

    print(name, "→", cholesterol, "→", status)
# cholestral patient deatails 

import pandas as pd
import matplotlib.pyplot as plt

# Read Excel file
df = pd.read_csv(r"C:\Users\HP\Desktop\Patient.csv")

# Assign colors based on cholesterol value
colors = []
for value in df["Cholesterol_mg_per_dL"]:
    if value < 200:
        colors.append("green")
    elif value < 240:
        colors.append("yellow")
    else:
        colors.append("red")

plt.style.use('bmh')

# Plot bar chart
plt.bar(df["Name"], df["Cholesterol_mg_per_dL"], color=colors)

plt.xlabel("Patient Name")
plt.ylabel("Cholesterol (mg/dL)")
plt.title("Patient-wise Cholesterol Levels")

plt.xticks(rotation=45)

# Threshold lines
plt.axhline(200, linestyle='--')
plt.axhline(240, linestyle='--')

plt.show()
# patient cholestral graph 

import pandas as pd 
data= pd.read_csv(r"C:\Users\HP\Desktop\tushi.csv")
print(df)

# Step 1: Filter Amit's data
amit_data = df[df['Name'].str.lower() == 'amit']

# Step 2: Get Amit's Heart Rate Category
amit_heart_rate = amit_data['Heart_Rate_Category']

print(amit_heart_rate)
# print amit heart rate 

import pandas as pd
data = pd.read_csv(r"C:\Users\HP\Desktop\Patient.csv", index_col="Name")

row = data.loc["Amit"]
print(row)
# amit patient deatils 

import pandas as pd
import numpy as np

data = pd.read_csv(r"C:\Users\HP\Desktop\tushi.csv", index_col="Name")

row = data.loc["Amit"]

# Extract heart rate values
hr_values = row[["Heart_Rate_bpm"]].values

# Calculate average heart rate
average_hr = np.mean(hr_values)
max_hr=np.max(hr_values)

print("Average Heart Rate for Amit:", average_hr)
print("max heart :", max_hr)
# print average and max heart rate 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

data = pd.read_csv(r"C:\Users\HP\Desktop\tushi.csv", index_col="Name")

row = data.loc["Amit"]
heart_rate = row.select_dtypes(include=[np.number])

# Line chart
plt.plot(heart_rate.index, heart_rate.values)

plt.xlabel("Days")
plt.ylabel("Heart_Rate_bpm")
plt.title("Amit Heart Rate Trend")

plt.show() 
# print heart rate trend graph (amit)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load file
df = pd.read_csv(r"C:\Users\HP\Desktop\tushi.csv", index_col="Name")

# Select Amit row
row = data.loc["Amit"]

# Select numeric calories burned values
Calories_Burned = row.select_dtypes(include=[np.number])

# Bar graph
plt.bar(df["Day"], df["Calories_Burned"])
plt.xlabel("Days")
plt.ylabel("Calories_Burned")
plt.title("Amit Calories Burned per Day")
plt.show()
# amit calories burned per day graph 

import pandas as pd

# Load file
df = pd.read_csv(r"C:\Users\HP\Desktop\tushi.csv")

# Loop directly over rows (no range)
for index, row in df.iterrows():
    if row["Name"] == "Amit":
        print("Amit on", row["Day"], "did", row["Activity"])
# activity 7 days 

import pandas as pd

# Load Excel / CSV file
df = pd.read_csv(r"C:\Users\HP\Desktop\tushi.csv")

# Loop through each patient
for i in range(len(df)):
    name = df.loc[i, "Name"]
    cp = df.loc[i, "Chest_Pain_Type"]

    if cp == 0:
        result = "Typical Angina"
    elif cp == 1:
        result = "Atypical Angina"
    elif cp == 2:
        result = "Non-anginal Pain"
    elif cp == 3:
        result = "Asymptomatic"

    print(name, "has", result)
# chest pain 

