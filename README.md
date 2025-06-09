# 🧪 Titanic Dataset - Exploratory Data Analysis (EDA)

This repository contains the Exploratory Data Analysis (EDA) project completed as part of **Task 5** in the Data Analyst Internship program.

## 📁 Dataset Used

- `train.csv`
- `test.csv`
- `gender_submission.csv`

Dataset source: [Kaggle - Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic/data)

## 🎯 Objective

To perform a detailed EDA on the Titanic dataset to extract insights, identify trends, and visualize relationships between different variables affecting passenger survival.

## 🛠 Tools Used

- Python
- Jupyter Notebook
- Pandas, NumPy
- Matplotlib, Seaborn

## 📊 EDA Highlights

### ✔ Univariate Analysis
- Survival Rate
- Gender Distribution
- Passenger Class Distribution
- Embarkation Port Frequencies

### ✔ Bivariate Analysis
- Survival vs. Gender
- Survival vs. Class
- Boxplots of Age by Survival

### ✔ Multivariate Analysis
- Correlation Heatmap
- Pairplot of key features

### ✔ Missing Values
- Imputed missing `Age` values with median
- Filled missing `Embarked` entries with mode
- `Cabin` largely missing; excluded from main analysis

## 📝 Deliverables

- `Titanic_EDA.ipynb`: Jupyter Notebook with complete EDA
- `EDA_Report.pdf`: PDF summary of visualizations and insights
- `README.md`: This file

## 📌 Key Findings

- Females had significantly higher survival rates than males.
- 1st class passengers had better chances of survival.
- Most passengers boarded from Southampton (`S`).
- Age and Fare show some influence on survival, but class and gender were more critical.

## 🚀 How to Run

1. Clone the repository
2. Open `Titanic_EDA.ipynb` in Jupyter Notebook
3. Run all cells to reproduce analysis and plots

```bash
git clone https://github.com/your-username/Titanic-EDA-Task5.git
cd Titanic-EDA-Task5
jupyter notebook Titanic_EDA.ipynb
