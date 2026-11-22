# MARKET BASKET ANALYSIS
# Beginner-friendly Python project using Pandas and Matplotlib

import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations

# Step 1: Load the transaction dataset
data = pd.read_csv("data/transactions.csv")

print("\nMARKET BASKET ANALYSIS")
print("----------------------")
print("Total transactions:", data["Transaction_ID"].nunique())
print("Total product entries:", len(data))

# Step 2: Count purchases of each product
product_count = data["Product"].value_counts()
product_result = product_count.reset_index()
product_result.columns = ["Product", "Purchase_Count"]
product_result.to_csv("outputs/product_purchase_count.csv", index=False)

print("\nMost purchased products:")
print(product_result.head(10).to_string(index=False))

# Step 3: Collect products belonging to each transaction
transaction_list = data.groupby("Transaction_ID")["Product"].apply(list)

# Step 4: Count pairs of products bought together
pair_count = {}

for product_list in transaction_list:
    # combinations creates pairs without repeating the same pair
    for pair in combinations(sorted(product_list), 2):
        if pair in pair_count:
            pair_count[pair] = pair_count[pair] + 1
        else:
            pair_count[pair] = 1

# Step 5: Calculate support for each pair
total_transactions = len(transaction_list)
pair_rows = []

for pair in pair_count:
    count = pair_count[pair]
    support = (count / total_transactions) * 100
    pair_rows.append([pair[0], pair[1], count, round(support, 2)])

pair_result = pd.DataFrame(
    pair_rows,
    columns=["Product_1", "Product_2", "Times_Bought_Together", "Support_Percent"]
)

pair_result = pair_result.sort_values(
    by="Times_Bought_Together", ascending=False
)

pair_result.to_csv("outputs/product_pair_analysis.csv", index=False)

print("\nTop product pairs bought together:")
print(pair_result.head(10).to_string(index=False))

# Step 6: Create a simple chart of the top 10 product pairs
top_pairs = pair_result.head(10).copy()
top_pairs["Pair_Name"] = top_pairs["Product_1"] + " + " + top_pairs["Product_2"]

plt.figure(figsize=(10, 6))
plt.barh(top_pairs["Pair_Name"], top_pairs["Times_Bought_Together"])
plt.xlabel("Number of Transactions")
plt.ylabel("Product Pair")
plt.title("Top 10 Products Frequently Bought Together")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("outputs/top_product_pairs.png")
plt.show()

# Step 7: Save a short business summary
best_pair = pair_result.iloc[0]
summary = [
    "MARKET BASKET ANALYSIS - SUMMARY",
    "--------------------------------",
    "Total transactions: " + str(total_transactions),
    "Most frequently purchased product: " + str(product_result.iloc[0]["Product"]),
    "Most common product pair: " + str(best_pair["Product_1"]) + " + " + str(best_pair["Product_2"]),
    "Times bought together: " + str(best_pair["Times_Bought_Together"]),
    "Support: " + str(best_pair["Support_Percent"]) + "%",
    "",
    "Business suggestion: The store can consider placing frequently paired products",
    "near each other or testing a combo offer. This is a suggestion for further testing,",
    "not proof that a promotion will increase sales."
]
with open("outputs/project_summary.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(summary))

print("\nAnalysis completed successfully.")
print("Check the outputs folder for CSV files, chart and summary.")
