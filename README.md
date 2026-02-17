# Amazon Sales Analysis

This project analyzes Amazon sales data to extract insights and visualize them in an interactive dashboard.

## Problem Statement

This project aims to answer the following questions:

*   Which regions have the highest total sales revenue?
*   What is the average unit price and unit cost for each item type?
*   Which country has the highest total profit?
*   How does the sales channel affect the order priority distribution?
*   What is the average order processing time (duration between order and ship dates) for each sales channel?
*   Which item types have the highest and lowest total sales?
*   How does the order priority vary across different regions?
*   What is the correlation between unit price and total profit?
*   Are there any seasonal trends or patterns in the sales data?
*   How does the number of units sold vary across different countries?

## Dataset

The dataset used is `Amazon Sales data.csv`, which contains information about orders, items, sales channels, and more.

## Approach

The analysis is performed using Python and popular data science libraries:

*   **Pandas:** For data manipulation and analysis.
*   **Matplotlib and Seaborn:** For data visualization.
*   **Streamlit:** To create an interactive web-based dashboard to present the findings.

The project is structured as follows:

1.  **Data Loading and Cleaning:** The `Amazon Sales data.csv` is loaded into a Pandas DataFrame, and initial data cleaning and preprocessing are performed.
2.  **Exploratory Data Analysis (EDA):** The data is explored to understand its structure, identify patterns, and answer the questions from the problem statement. This is done in the `Analyzing Amazon Sales data.ipynb` notebook.
3.  **Dashboard Development:** An interactive dashboard is created using Streamlit in the `app.py` file to visualize the insights.

## Technologies Used

*   Python
*   Pandas
*   Matplotlib
*   Seaborn
*   Streamlit

## How to Run the Project

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Amazon-Sales-Analysis.git
    ```
2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

## Author

*   **LinkedIn:** [Motilal Das](https://www.linkedin.com/in/motilal-das-42b4a9254/?lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3BVXKFc19ASZq05NOB7VosAg%3D%3D)
*   **GitHub:** [MkSingh431]([text](https://github.com/MkSingh431/Amazon_Sales_Analysis))