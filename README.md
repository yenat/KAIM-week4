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
    ```

3. Run the cells in the notebook to perform the analysis and visualize the results.
