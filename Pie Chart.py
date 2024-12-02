#Pie Chart

import matplotlib.pyplot as plt
import pandas as pd

# Reading the tips.csv file
data = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/tips.csv')

# Initializing the data for the pie chart
cars = ['AUDI', 'BMW', 'FORD', 'TESLA', 'JAGUAR']
data = [23, 10, 35, 15, 12]  # Example data values

# Creating the pie chart
plt.pie(data, labels=cars, autopct='%1.1f%%', startangle=140)

# Adding title to the plot
plt.title("Car Data")

# Displaying the plot
plt.show()
