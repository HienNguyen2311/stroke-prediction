# Exploring Relationship Between Health Risk Factors and Stroke

This project aims to identify the important risk factors for stroke using data from the National Health and Nutrition Examination Survey (NHANES). It focuses on demographic and questionnaire data to quickly identify people at risk of stroke before conducting further lab tests. The analysis is performed using Python and various data science libraries.

## Features

- Data preprocessing and cleaning
- Exploratory data analysis (EDA) including visualizations 
- Feature selection using Random Forest
- Logistic Regression to determine effect sizes of risk factors
- Interactive dashboard to explore findings

## Installation

1. Clone this repository
2. Install the required Python packages: pandas, numpy, matplotlib, scikit-learn, statsmodels, scipy, functools, plotly, dash


## Usage

1. Run the Jupyter notebooks and Python file in the following order:
- `project_data_preparation.ipynb`
    * Imports libraries and defines functions to merge data frames
    * Creates data frames for different years (2017-2018, 2015-2016, 2013-2014)
    * Merges data frames from different years
    * Checks and removes duplicate rows
    * Explores data structure and handles missing values
    * Saves the cleaned dataset as `data_MCQ160F_eda.csv`
    * Uses Random Forest classifier to identify important risk factors
    * Fits the model and obtains feature importance scores

- `project-main-analysis.ipynb` 
    * Loads the cleaned dataset
    * Performs EDA (VIF, correlation analysis, distribution analysis)
    * Focuses on selected features from previous step
    * Explores feature interactions
    * Splits data into training and testing sets
    * Applies data preprocessing (encoding, scaling, imputation)
    * Performs logistic regression to determine effect sizes
    * Trains the model and obtains regression results
    * Exports results as `results.csv`
    * Applies threshold-moving techniques and evaluates model performance
    
- `project-dashboard.py`
    * Includes visualizations (histograms, scatter plots, stacked bar charts)
    * Provides an interactive table of logistic regression results
    * Allows exploration of relationships between features and stroke risk

2. Launch the interactive dashboard:
- Open a web browser and go to `http://127.0.0.1:4567/` to view the dashboard.

## Data Sources
National Health and Nutrition Examination Survey (NHANES) 2013-2018 data files: https://wwwn.cdc.gov/nchs/nhanes/Default.aspx
- Demographics
- Examination
- Laboratory
- Questionnaire

## Technologies Used

Python 3, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Plotly Dash

## Samples Visualizations

Categorical predictors' values count

![dashboard1](https://github.com/user-attachments/assets/437c1802-c263-41ef-8764-0d64bd995230)

Numerous predictors' values count

![dashboard2](https://github.com/user-attachments/assets/0b037526-b5fc-4a31-b2f5-8864070cfa70)

Predictors relationship

![dashboard3](https://github.com/user-attachments/assets/bdaf9829-afa1-46ae-b5bd-158e6b49cdf5)

## License

This project is licensed under the MIT License.

## Project Report

This project explores the relationship between various health risk factors and stroke using data from the National Health and Nutrition Examination Survey (NHANES). The analysis focuses primarily on demographic and questionnaire data to identify people at risk of stroke before conducting further lab tests.

Key points:

1. Methodology:

* Random Forest algorithm to identify important risk factors
* Logistic Regression to determine effect sizes of risk factors
* MICE imputation for handling missing data

2. Key findings:

* Significant risk factors include high blood pressure, high cholesterol, limited work ability, diabetes, age (especially over 70), and creatinine levels.
* Physical activities like walking, bicycling, and moderate recreational activities are associated with lower stroke risk.
* Education level and race show some correlation with stroke risk.

3. Ethical considerations:

* Potential sampling biases due to self-reported diagnoses
* Imbalanced representation of certain demographic groups
* Privacy concerns with sensitive health data

4. Limitations:

* Model performance shows high sensitivity but low specificity
* Dataset may not be representative of populations outside the US

5. Future work:

* Collect more balanced data, especially for underrepresented groups
* Adapt the model for use in other countries (e.g., New Zealand)
* Implement fairness metrics to monitor potential biases
