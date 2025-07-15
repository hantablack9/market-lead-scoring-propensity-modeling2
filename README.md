# market-lead-scoring-propensity-modeling2

[![Release](https://img.shields.io/github/v/release/hantablack9/market-lead-scoring-propensity-modeling2)](https://img.shields.io/github/v/release/hantablack9/market-lead-scoring-propensity-modeling2)
[![Build status](https://img.shields.io/github/actions/workflow/status/hantablack9/market-lead-scoring-propensity-modeling2/main.yml?branch=main)](https://github.com/hantablack9/market-lead-scoring-propensity-modeling2/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/hantablack9/market-lead-scoring-propensity-modeling2/branch/main/graph/badge.svg)](https://codecov.io/gh/hantablack9/market-lead-scoring-propensity-modeling2)
[![Commit activity](https://img.shields.io/github/commit-activity/m/hantablack9/market-lead-scoring-propensity-modeling2)](https://img.shields.io/github/commit-activity/m/hantablack9/market-lead-scoring-propensity-modeling2)
[![License](https://img.shields.io/github/license/hantablack9/market-lead-scoring-propensity-modeling2)](https://img.shields.io/github/license/hantablack9/market-lead-scoring-propensity-modeling2)

This is a project to deliver a machine learning model which qualifies leads for the sales department of an ed-tech platform.

- **Github repository**: <https://github.com/hantablack9/market-lead-scoring-propensity-modeling2/>
- **Documentation** <https://hantablack9.github.io/market-lead-scoring-propensity-modeling2/>


# 🧠 Lead Scoring Using ML Algorithms – Capstone Project

## 📌 Problem Statement

In this capstone project, you are required to analyze a dataset and build a machine learning model that predicts the **propensity of a lead to purchase a course**. The objective is to help improve sales effectiveness by identifying high-conversion leads.

---

## 📂 Dataset

**File:** `Purchase_Fraud_Data.csv`
Each row represents a lead with detailed attributes about their interaction, behavior, and metadata regarding the lead acquisition and sales journey.

---

## 📝 Dataset Description

| Column Name                   | Description |
|------------------------------|-------------|
| `opportunity_id`             | Unique ID of the lead |
| `stagename`                  | Current stage of the lead |
| `subsource`                  | Subsource of the lead |
| `unanswered_call_counter`    | Number of unanswered calls |
| `unserviced age`             | Days since no action on lead |
| `ageing`                     | Days since lead was created |
| `source`                     | Source of the lead |
| `Opportunity_created_date`   | Date of lead generation |
| `time_taken_for_allocation` | Time to allocate lead to salesperson |
| `no_of_calls`                | Number of calls made |
| `calldurationinseconds`      | Duration of sales calls |
| `City`                       | Lead’s city |
| `City Type`                  | Tier classification of the city |
| `Workexp`                    | Work experience of the lead |
| `Laststagechangedate`        | Date when lead stage was changed |
| `Sales_end_date`             | End date of sales cycle |
| `Sales_start_date`           | Start date of sales cycle |
| `Program_number`             | Program identifier |
| `Program Code -Renewed`      | Renewed program code |
| `total_program_fee.1`        | Program fees |
| `Category`                   | Program category |
| `Is_serviced_c`              | Whether lead was serviced |
| `Business_vertical`          | Business vertical of program |
| `Budget`                     | Budget for the program |
| `Lastactivitydate`           | Last interaction with the lead |
| `Institute`                  | Program institute |
| `Year`                       | Year of lead generation |
| `Month`                      | Month of lead generation |
| `Month_name`                 | Name of the month |
| `Week of Year`               | Week number in the year |
| `Week of Month`              | Week number in the month |
| `Day of Year`                | Day number in the year |
| `Day of Week`                | Day number in the week |
| `Day Name`                   | Day name (e.g. Monday) |
| `Age`                        | Age range of the lead |
| `is_session_Working_day`     | Is the session on a working day |
| `workex_reqd`                | Work experience required |
| `Session_Start_day_inweek`   | Day session starts |
| `Weekly_sessionsdays_count` | Count of sessions per week |
| `sales_Working_day`          | Working day for sales |
| `Time`                       | Lead generation time |
| `Hour`                       | Hour of the day |
| `IscreatedinWorking_hour`    | Created during sales hours |
| `Funnel_category`            | Simplified lead stage for target variable |

---

## 📈 Project Outline

### 1. Exploratory Data Analysis (EDA)

- **Descriptive Statistics**
  - Summarize numerical, categorical, and date columns.
  - Note key trends and anomalies.

- **Missing Value Treatment**
  - Identify nulls and treat using suitable techniques.

- **Univariate Analysis**
  - Numerical: Distribution plots, histograms
  - Categorical: Frequency bar plots

- **Multivariate Analysis**
  - Categorical vs Numerical: Bar plots, boxplots
  - Numerical vs Numerical: Scatter plots, heatmaps
  - Categorical vs Multiple Numericals: Group-wise distributions
  - Correlation matrix to evaluate multicollinearity

---

### 2. Feature Engineering

- Create meaningful new features from date/time columns.
- Transform skewed distributions.
- Encode categorical features appropriately.
- Engineer interaction terms or composite metrics where applicable.

---

### 3. Model Building

- Prepare dataset with cleaned and engineered features.
- Train baseline models (e.g., Logistic Regression, Decision Trees).
- Evaluate using precision, recall, F1-score, ROC-AUC.
- Tune hyperparameters for performance optimization.
- Optionally ensemble models for better generalization.

---

## 🚀 Objective

Deliver a well-performing, interpretable machine learning model that helps prioritize leads likely to convert, thereby improving sales efficiency.

---

## 📧 Contact

For any clarification, reach out via project collaboration channel or [email.](hanishpaturi1320@gmail.com).

<!-- 
## Getting started with your project

### 1. Create a New Repository

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:hantablack9/market-lead-scoring-propensity-modeling2.git
git push -u origin main
```

### 2. Set Up Your Development Environment

Then, install the environment and the pre-commit hooks with

```bash
make install
```

This will also generate your `uv.lock` file

### 3. Run the pre-commit hooks

Initially, the CI/CD pipeline might be failing due to formatting issues. To resolve those run:

```bash
uv run pre-commit run -a
```

### 4. Commit the changes

Lastly, commit the changes made by the two steps above to your repository.

```bash
git add .
git commit -m 'Fix formatting issues'
git push origin main
```

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.

To finalize the set-up for publishing to PyPI, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/codecov/).

## Releasing a new version



---

Repository initiated with [fpgmaas/cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv). -->
