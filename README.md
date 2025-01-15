# Customer Purchasing Behavior Analysis

This repository contains a comprehensive analysis of customer purchasing behavior across various stores. The project focuses on understanding how different factors such as promotions, holidays, assortment types, and competition impact sales. The analysis is performed using Python in Jupyter Notebooks.

## Table of Contents

- [Project Overview](#project-overview)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Key Findings](#key-findings)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The goal of this project is to explore the behavior of customers and analyze the impact of various factors on sales. The analysis includes:
- Checking the distribution of promotions in training and test sets
- Comparing sales behavior before, during, and after holidays
- Identifying seasonal purchase behaviors
- Correlating sales with the number of customers
- Examining the effect of promotions on sales
- Analyzing customer behavior during store opening and closing times
- Investigating the impact of assortment types and competition on sales

## Directory Structure

```plaintext
├── notebooks
│   ├── customer_behavior_analysis.ipynb
│   ├── README.md
├── data
│   ├── train.csv
│   ├── test.csv
│   ├── store.csv
├── requirements.txt
├── README.md
```

## Installation

To run the analysis, you need to have Python installed. Follow these steps to set up the environment:

1. Clone the repository:
    ```bash
    git clone <repository-URL>
    ```

2. Navigate to the project directory:
    ```bash
    cd <repository-directory>
    ```

3. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Navigate to the `notebooks` directory:
    ```bash
    cd notebooks
    ```

2. Open the Jupyter Notebook:
    ```bash
    jupyter notebook customer_behavior_analysis.ipynb 
    jupyter notebook build_model.ipynb 
    jupyter notebook lstm_model.ipynb
    ```

3. Run the cells in the notebook to perform the analysis and visualize the results.

## Key Findings
### Customer Behavior Analysis:

Promotional campaigns significantly boost sales.

December shows peak sales due to holiday shopping.

Sundays have the highest average sales compared to other weekdays.

Sales drop on Fridays and Saturdays.

Proximity to competitors has minimal impact on sales.

A wider product assortment attracts more customers.

### Sales Prediction:

Machine Learning Model: The machine learning model achieved a training MSE of 0.0215 and a validation MSE of 0.1555. This indicates strong performance on the training data but a decline in accuracy on the validation data, suggesting potential overfitting.

Deep Learning Model: The deep learning model using an LSTM network demonstrated effective learning from the data. The training and validation loss plots showed decreasing loss over epochs, indicating good generalization to new data.