"""Install pandas using one of the following commands
  - conda install pandas (prefer this one)
  - pip install pandas
"""
import pandas as pd

data = {"apples": [3, 2, 0, 1], "oranges": [0, 3, 7, 2]}

purchase = pd.DataFrame(data)

print(purchase)

purchase = pd.DataFrame(data, index=["June", "Robert", "Lily", "David"])

print(purchase)

print("Here is the line for 'June'")
print(purchase.loc["June"])


df = pd.read_csv("../data/purchase.csv")

print(df)


df = pd.read_csv("../data/purchase.csv", index_col=0)

print(df)

df = pd.read_json("../data/sample.json")

print(df)


import sqlite3

# conn = sqlite3.connect("database.db")

# db = pd.read_sql_query("select * from purchase", conn)
with sqlite3.connect("database.db") as conn:
    db = pd.read_sql_query("select * from purchase", conn)

# db.set_index('indexs',inplace=True)

db = db.set_index("indexs")


print(db)

data = {"apples": [3, 2, 0, 1], "oranges": [0, 3, 7, 2]}

purchase = pd.DataFrame(data)


purchase = pd.DataFrame(data, index=["June", "Robert", "Lily", "David"])


print(purchase)

purchase.to_csv("local_data/new_purchase.csv")
purchase.to_json("local_data/new_purchase.json")

purchase.to_sql("new_purchase", conn)
