import sqlite3
import pandas as pd

conn = sqlite3.connect("order.db")

def get_county_orders(conn, county, start_date, end_date):
    query = """
        SELECT product,
            COUNT(*) AS total_orders,
            SUM(quantity) AS total_quantity,
            SUM(total_value) AS total_revenue_kes
        FROM orders
        WHERE county = ? 
            AND order_date BETWEEN ? AND ?
        GROUP BY product
        ORDER BY total_value DESC
    """
    df = pd.read_sql_query(query, conn, params=(county, start_date, end_date))

    if df.empty:
        print(f"No orders found for {county} between {start_date} and {end_date}.")
    else:
        print(df)

    return df

conn = sqlite3.connect("order.db")

get_county_orders(conn, "Eldoret", "2026-05-27", "2026-06-28")

print()

get_county_orders(conn, "Nairobi", "2026-08-26", "2026-09-02")
