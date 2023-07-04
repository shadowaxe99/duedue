```python
import os
import pandas as pd
from sklearn.model_selection import train_test_split

# Define the path to the dataset
dataset_path = "path_to_your_dataset.csv"

# Load the dataset
df = pd.read_csv(dataset_path)

# Check if the dataset is loaded correctly
print(df.head())

# Split the dataset into training and validation sets
train_df, val_df = train_test_split(df, test_size=0.2, random_state=42)

# Define the paths to save the training and validation sets
train_path = "train.csv"
val_path = "val.csv"

# Save the training and validation sets
train_df.to_csv(train_path, index=False)
val_df.to_csv(val_path, index=False)

# Print the number of articles in the training and validation sets
print(f"Number of articles in the training set: {len(train_df)}")
print(f"Number of articles in the validation set: {len(val_df)}")
```