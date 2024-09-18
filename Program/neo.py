import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings


url = '/kaggle/input/nasa-nearest-earth-objects-1910-2024/nearest-earth-objects(1910-2024).csv'

# Load the dataset into a pandas DataFrame
df = pd.read_csv(url)

# Display the first few rows of the DataFrame to ensure it is loaded correctly
print(df.head())