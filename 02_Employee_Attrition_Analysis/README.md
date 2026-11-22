# Employee Attrition Analysis

## Project overview
This project explores a sample employee dataset to understand employee attrition (employees who leave an organization). It compares attrition across departments, job satisfaction levels and average monthly income.

## Objective
- Count employees who left and employees who stayed.
- Calculate the overall attrition rate.
- Compare the number of employees who left across departments.
- Compare average monthly income for employees who left and stayed.
- Explore attrition counts by job satisfaction score.
- Create simple charts to communicate the findings.

## Technology used
- Python
- Pandas
- Matplotlib

## Project structure
```text
02_Employee_Attrition_Analysis/
|-- data/
|   `-- employee_data.csv
|-- outputs/
|-- main.py
|-- requirements.txt
`-- README.md
```

## Dataset and privacy
`data/employee_data.csv` is a synthetic sample dataset created for this learning project. It contains no real employee records or personal information. The sample has 150 fictional employee rows.

## How to run
1. Install Python 3.
2. Download or clone this project folder.
3. Open a terminal inside `02_Employee_Attrition_Analysis`.
4. Install the required packages:
   `pip install -r requirements.txt`
5. Run:
   `python main.py`

The program creates the `outputs` files automatically. It may open two chart windows; close each window to continue.

## Output files
- `department_attrition.csv`: number of employees who left in each department.
- `average_income_by_attrition.csv`: average monthly income grouped by attrition status.
- `attrition_by_satisfaction.csv`: number of employees who left for each satisfaction score.
- `department_attrition.png`: department-wise bar chart.
- `attrition_count.png`: left-versus-stayed bar chart.
- `project_summary.txt`: short project summary.

## Analysis note
The charts show patterns in the included sample only. They do not establish why an employee left. HR teams should use real, authorized and anonymized company data and investigate other factors before making decisions.
