# Análisis de Ventas de una Tienda Online

Este proyecto demuestra un pipeline ETL para procesar datos de ventas de una tienda online. El objetivo es extraer datos de diversas fuentes, transformarlos para limpiar y normalizar la información, y cargarlos en una base de datos para su posterior análisis.

## Tecnologías Utilizadas
- Python
- pandas
- requests
- SQLAlchemy
- SQLite

## Cómo Configurar el Proyecto

1. Clona el repositorio:
   ```bash
   git clone https://github.com/B3nj4-U/etl-sales-analysis.git
   cd etl-sales-analysis

2. Crea un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt

4. Crea los archivos de datos:
   ```bash
   sales_data.csv
   customers_data.json

5. Ejecuta el script ETL:
   ```bash
   python etl_pipeline.py

6. Ejecuta el script check_data para comprobaciones:
   ```bash
   python check_data.py

## Estructura del proyecto
etl_pipeline.py: Script principal que ejecuta el proceso ETL. Extrae datos desde archivos CSV y JSON, realiza transformaciones y carga los datos en una base de datos SQLite.

sales_data.csv: Archivo de datos ficticios de ventas. Contiene registros de ventas con campos como fecha, ID de producto, ID de cliente, monto de la venta, nombre del producto y categoría.

customers_data.json: Archivo de datos ficticios de clientes. Incluye información de clientes como ID, nombre y correo electrónico, utilizada para enriquecer los datos de ventas en el proceso ETL.

check_data.py: Script para realizar comprobaciones de los datos cargados en la base de datos. Imprime el contenido de las tablas para verificar que el proceso ETL ha sido exitoso y los datos están correctos.

README.md: Documentación del proyecto que proporciona una guía sobre los requisitos, la instalación, el uso y la estructura del proyecto.
