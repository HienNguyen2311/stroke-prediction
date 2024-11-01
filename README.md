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
- `project-main-analysis.ipynb` 
- `project-dashboard.py`

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

## Visualizations

## License

This project is licensed under the MIT License.

## Project Report

This project explores the relationship between various health risk factors and stroke using data from the National Health and Nutrition Examination Survey (NHANES). The analysis focuses primarily on demographic and questionnaire data to identify people at risk of stroke before conducting further lab tests.

Key points:

1. Methodology:

*Random Forest algorithm to identify important risk factors
*Logistic Regression to determine effect sizes of risk factors
*MICE imputation for handling missing data

2. Key findings:

*Significant risk factors include high blood pressure, high cholesterol, limited work ability, diabetes, age (especially over 70), and creatinine levels.
*Physical activities like walking, bicycling, and moderate recreational activities are associated with lower stroke risk.
*Education level and race show some correlation with stroke risk.

3. Ethical considerations:

*Potential sampling biases due to self-reported diagnoses
*Imbalanced representation of certain demographic groups
*Privacy concerns with sensitive health data

4. Limitations:

*Model performance shows high sensitivity but low specificity
*Dataset may not be representative of populations outside the US

5. Future work:

*Collect more balanced data, especially for underrepresented groups
*Adapt the model for use in other countries (e.g., New Zealand)
*Implement fairness metrics to monitor potential biases