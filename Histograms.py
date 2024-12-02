#Program for Histograms

import matplotlib.pyplot as plt
import pandas as pd

# Reading the tips.csv file
data = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/tips.csv')

# Extracting the 'total_bill' column for plotting
x = data['total_bill']

# Plotting the histogram
plt.hist(x, bins=25, color='green', edgecolor='blue', linestyle='--', alpha=0.5)

# Adding title and labels
plt.title("Tips Dataset")
plt.xlabel('Total Bill')
plt.ylabel('Frequency')

# Displaying the plot
plt.show()
