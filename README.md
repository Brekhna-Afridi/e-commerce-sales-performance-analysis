# E-Commerce Sales Performance Analysis

A portfolio-ready Data Analyst project using Python and Pandas to analyze e-commerce sales performance, order status, product/category performance, fulfilment, and geographic patterns.

## Project Goal

The analysis follows a practical data-analysis workflow:

**Data Understanding → Data Wrangling → Missing-Value Analysis → EDA → Business Questions → Visualization → Insights → Export → Dashboard**

## Tools

- Python
- Pandas
- NumPy
- Matplotlib
- Plotly
- Streamlit
- Jupyter Notebook / Google Colab

## Dataset

The source dataset contains 128,975 rows and 17 columns before cleaning.

Date coverage in the source data: **2022-03-31 to 2022-06-29**.

### Missing-value treatment

The project keeps the user's original business logic:

- `ship-city`, `ship-state`, and `ship-postal-code` had a very small proportion of missing values, so affected rows were removed.
- `Amount` is required for value-based analysis, so rows with missing `Amount` were removed rather than assigning an artificial value.
- `Courier Status` was investigated before treatment. Of the 6,872 missing `Courier Status` values, 6,861 were associated with `Cancelled` status. Therefore missing `Courier Status` values were labelled `Cancelled` to preserve those records.

After duplicate removal and the documented cleaning steps, the analysis dataset contains **121,146 rows**.

## Key Analysis Areas

1. Data quality and missing values
2. Duplicate detection
3. Numeric validation
4. Order-status distribution
5. Fulfilment analysis
6. Category performance
7. Top product styles
8. State-level sales patterns
9. Monthly reported vs delivered order value
10. Quantity vs amount relationship
11. Interactive dashboard

## Selected Findings

- **Set** is the highest reported-value category.
- **JNE3797** is the highest reported-value style.
- **Maharashtra** has the highest reported order value among states.
- **Amazon** has the larger reported order value among fulfilment methods.
- **Shipped** is the most common order status after cleaning.
- Quantity and amount have a relatively weak linear correlation in this dataset.

> `Amount` is treated as reported order-line value. Because the dataset includes cancellations and returns, it should not automatically be interpreted as recognized revenue.

## Repository Structure

```text
e-commerce-sales-performance-analysis/
│
├── E-Commerce_Sales_Performance_Analysis.ipynb
├── dashboard.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── data/
    ├── raw/
    │   └── datapro.csv
    └── processed/
        └── amazon_sales_cleaned.csv
```

## Run the Notebook

Install dependencies:

```bash
pip install -r requirements.txt
```

Open:

```text
E-Commerce_Sales_Performance_Analysis.ipynb
```

## Run the Dashboard

From the project folder:

```bash
pip install -r requirements.txt
streamlit run dashboard.py
```

## Portfolio Value

This project demonstrates practical skills in:

- Data cleaning and validation
- Missing-value analysis
- Pandas `groupby`, `agg`, filtering, and sorting
- Exploratory data analysis
- Business-question-driven analysis
- Data visualization
- KPI development
- Interactive dashboard development
- Communicating data-quality decisions and business insights

## Important Note

Before making the repository public, verify that the original dataset can legally be redistributed. If the dataset has usage restrictions, keep the raw file private and publish only an allowed sample/processed version plus the dataset source information.
