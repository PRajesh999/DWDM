#Bar Charts

import matplotlib.pyplot as plt
import pandas as pd

# Reading the tips.csv file
data = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/tips.csv')

# Initializing the data for the bar plot
x = data['day']               
y = data['total_bill']        

# Creating the bar plot
plt.bar(x, y, color='green', edgecolor='blue', linewidth=2)

# Adding title and labels
plt.title("Tips Dataset")
plt.xlabel('Day')
plt.ylabel('Total Bill')

# Displaying the plot
plt.show()
