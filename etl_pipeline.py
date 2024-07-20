import pandas as pd
import requests
from sqlalchemy import create_engine

# Leer datos de ventas desde CSV
sales_df = pd.read_csv('sales_data.csv')

# Leer datos de clientes desde JSON
customers_df = pd.read_json('customers_data.json')

# Simular una llamada a una API para obtener datos de productos
def fetch_products_data():
    return [
        {"product_id": 101, "product_name": "Widget", "category": "Gadgets"},
        {"product_id": 102, "product_name": "Gizmo", "category": "Gadgets"},
        {"product_id": 103, "product_name": "Doodad", "category": "Tools"}
    ]

products_df = pd.DataFrame(fetch_products_data())

# Limpieza de datos
sales_df.drop_duplicates(inplace=True)
sales_df.fillna(0, inplace=True)

# Enriquecimiento de datos
if 'product_id' in sales_df.columns and 'product_id' in products_df.columns:
    sales_df = sales_df.merge(products_df, on='product_id', how='left')
else:
    print("Error: La columna 'product_id' no existe en uno de los DataFrames.")

# Agregación de datos
if 'date' in sales_df.columns:
    daily_sales = sales_df.groupby('date').agg({
        'sales_amount': 'sum',
        'product_id': 'count'
    }).rename(columns={'sales_amount': 'total_sales', 'product_id': 'total_products_sold'})
else:
    print("Error: La columna 'date' no existe en el DataFrame de ventas.")

# Crear una conexión a la base de datos SQLite
engine = create_engine('sqlite:///sales_analysis.db')

# Cargar los datos transformados en la base de datos
sales_df.to_sql('sales', engine, if_exists='replace', index=False)
daily_sales.to_sql('daily_sales', engine, if_exists='replace', index=False)

print("Proceso ETL completado con éxito")