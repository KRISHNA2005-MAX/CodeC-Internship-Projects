# Market Basket Analysis

## Project overview
This project studies shopping transactions to find products that customers frequently buy together. A store can use this information to explore product placement and combo-offer ideas.

## Objective
- Count how often each product is purchased.
- Find product pairs that appear in the same transaction.
- Calculate pair support as a percentage of all transactions.
- Present the most common pairs in a chart.

## Technology used
- Python
- Pandas
- Matplotlib

## Project structure
```text
01_Market_Basket_Analysis/
|-- data/
|   `-- transactions.csv
|-- outputs/
|-- main.py
|-- requirements.txt
`-- README.md
```

## Dataset
`data/transactions.csv` is a small sample grocery transaction dataset included with this project. Each row represents one product in one transaction. The data is prepared for learning and is not a real retailer's customer data.

## How to run
1. Install Python 3.
2. Download or clone this project folder.
3. Open a terminal inside `01_Market_Basket_Analysis`.
4. Install the required packages:
   `pip install -r requirements.txt`
5. Run:
   `python main.py`

The program creates the `outputs` files automatically. It may open a chart window; close the window to finish running.

## Output files
- `product_purchase_count.csv`: purchase count for each product.
- `product_pair_analysis.csv`: product pairs, count and support percentage.
- `top_product_pairs.png`: bar chart of the top 10 pairs.
- `project_summary.txt`: short text summary and business suggestion.

## Method
The code groups products by transaction and checks product pairs using Python's `combinations`. Support is calculated as:

`Support (%) = (Transactions containing the pair / Total transactions) * 100`

## Key learning
This is a basic frequency-based market basket project. It does not claim to implement the Apriori algorithm or advanced association-rule mining.

## Business interpretation
Frequently paired products may be candidates for nearby shelf placement or a combo-offer experiment. A retailer should test such ideas and measure the results before making business decisions.
