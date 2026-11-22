# EMPLOYEE ATTRITION ANALYSIS
# Beginner-friendly Python project using Pandas and Matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load employee data
data = pd.read_csv("data/employee_data.csv")

print("\nEMPLOYEE ATTRITION ANALYSIS")
print("---------------------------")
print("Total employees:", len(data))

# Step 2: Check the dataset
print("\nFirst five records:")
print(data.head())

# Step 3: Count employees who left and stayed
attrition_count = data["Attrition"].value_counts()
print("\nEmployees who left or stayed:")
print(attrition_count)

employees_left = (data["Attrition"] == "Yes").sum()
total_employees = len(data)
attrition_rate = (employees_left / total_employees) * 100

print("\nEmployees who left:", employees_left)
print("Overall attrition rate:", round(attrition_rate, 2), "%")

# Step 4: Department-wise attrition count
department_result = data[data["Attrition"] == "Yes"].groupby("Department").size()
department_result = department_result.sort_values(ascending=False)

print("\nEmployees who left from each department:")
print(department_result)

department_result.to_csv("outputs/department_attrition.csv")

# Step 5: Average income for employees who left and stayed
income_result = data.groupby("Attrition")["Monthly_Income"].mean()

print("\nAverage monthly income:")
print(income_result.round(2))

income_result.to_csv("outputs/average_income_by_attrition.csv")

# Step 6: Attrition by job satisfaction
satisfaction_result = data[data["Attrition"] == "Yes"].groupby(
    "Job_Satisfaction"
).size()

print("\nEmployees who left by job satisfaction score:")
print(satisfaction_result)

satisfaction_result.to_csv("outputs/attrition_by_satisfaction.csv")

# Step 7: Create department-wise attrition chart
plt.figure(figsize=(9, 5))
department_result.plot(kind="bar")
plt.title("Employees Who Left by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.xticks(rotation=20, ha="right")
plt.tight_layout()
plt.savefig("outputs/department_attrition.png")
plt.show()

# Step 8: Create attrition count chart
plt.figure(figsize=(6, 4))
attrition_count.plot(kind="bar")
plt.title("Employee Attrition Count")
plt.xlabel("Attrition")
plt.ylabel("Number of Employees")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("outputs/attrition_count.png")
plt.show()

# Step 9: Save project summary
summary = [
    "EMPLOYEE ATTRITION ANALYSIS - SUMMARY",
    "-------------------------------------",
    "Total employees: " + str(total_employees),
    "Employees who left: " + str(employees_left),
    "Overall attrition rate: " + str(round(attrition_rate, 2)) + "%",
    "",
    "Department-wise counts and average income are available in the outputs folder.",
    "Use these findings as starting points for HR investigation, not as proof of causes."
]
with open("outputs/project_summary.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(summary))

print("\nAnalysis completed successfully.")
print("Check the outputs folder for CSV files, charts and summary.")
