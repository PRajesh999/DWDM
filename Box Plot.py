#Box Plot

# Importing the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Enable inline plotting for Jupyter or Colab
%matplotlib inline  

# Load the dataset
df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/tips.csv")

# Display the first 5 rows of the dataset
df.head()

# Set the plot style
sns.set_style("whitegrid")

# Create a boxplot showing 'total_bill' distribution for each 'day'
sns.boxplot(x='day', y='total_bill', data=df)

# Add a title to the plot
plt.title("Boxplot of Total Bill by Day")

# Display the plot
plt.show()
