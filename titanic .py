# Importing necessary libraries for EDA
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the Titanic dataset
train_df = pd.read_csv("/mnt/data/train.csv")
test_df = pd.read_csv("/mnt/data/test.csv")
gender_df = pd.read_csv("/mnt/data/gender_submission.csv")

# Basic information about the dataset
train_info = train_df.info()
train_description = train_df.describe(include='all')

# Checking for missing values
missing_values = train_df.isnull().sum()

# Preview of the dataset
train_head = train_df.head()

train_info, train_description, missing_values, train_head