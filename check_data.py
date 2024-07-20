import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('sales_analysis.db')
cursor = conn.cursor()

# Consultar la tabla 'sales'
cursor.execute('SELECT * FROM sales')
sales_data = cursor.fetchall()
print("Datos de ventas:")
for row in sales_data:
    print(row)

# Consultar la tabla 'daily_sales'
cursor.execute('SELECT * FROM daily_sales')
daily_sales_data = cursor.fetchall()
print("\nDatos de ventas diarias:")
for row in daily_sales_data:
    print(row)

# Cerrar la conexión
conn.close()
