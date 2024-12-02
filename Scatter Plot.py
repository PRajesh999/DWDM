#Scatter Plot

import matplotlib.pyplot as plt
import pandas as pd

# Reading the tips.csv file
data = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/tips.csv')

# Initializing the data for the scatter plot
x = data['day']               # Days of the week
y = data['total_bill']        # Total bill amounts

# Creating the scatter plot
plt.scatter(x, y, 
            c=data['size'],            # Color based on the group size
            s=data['total_bill'],      # Size of markers based on the total bill
            marker='D',                # Diamond-shaped markers
            alpha=0.5)                 # Transparency level

# Adding title and labels
plt.title("Tips Dataset")
plt.xlabel('Day')
plt.ylabel('Total Bill')

# Displaying the plot
plt.show()
