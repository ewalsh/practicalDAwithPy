import sqlite3
import pandas as pd

conn = sqlite3.connect('./data/customer_sales.db')

df_sales = pd.read_sql_query("SELECT * FROM tbl_sales;",conn)

print(df_sales[(df_sales['Sales_Quantity'] == 1)])
