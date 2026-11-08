# File: README.md

# Nairobi Wholesale Distributor Sales-Record Analysis

A Python script that returns orders for any county and date range for distributor's operations team.

## What It Does

- Connects Python to the SQLite
- Runs the SQL query
- Uses parameterized queries to prevent bad input from altering or deleting your database
- It replaces the rewritng of the query for every question since this code is reusable

## Setup

```bash
pip install pandas
```

## Usage

Run the program from the project's folder where the database file(order.db) is saved. 
```
python param_query.py
```

## How It Works

Connects to the database and then filters for specific data(county and date range).

 
```python
conn = sqlite3.connect("order.db")

get_county_orders(conn, "Eldoret", "2026-05-27", "2026-06-28")

get_county_orders(conn, "Nairobi", "2026-08-26", "2026-09-02")
```

## Sample Output
```
No orders found for Eldoret between 2026-05-27 and 2026-06-28.

           product  total_orders  total_quantity  total_revenue_kes
0        Rice 25kg             1              35           112000.0
1  Maize Flour 2kg             2             130            15600.0
```

## Stack

Python, SQL, Pandas


## Pricing Note

KES 55,000 for such reusable scritp that will save your time. 
