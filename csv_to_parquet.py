import duckdb

tb_orders = duckdb.read_csv(f"data/upload/csv/olist_orders_dataset.csv")

sink = duckdb.sql("SELECT * FROM 'tb_orders'")
sink.show()

duckdb.sql(f"""COPY tb_orders TO 'data/raw/orders/tb_orders.parquet' (FORMAT PARQUET)""")

