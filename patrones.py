
import pandas as pd
import matplotlib.pyplot as plt

#HISTOGRAMA DE 'Bottles Sold'

# Lee el archivo CSV
data = pd.read_csv('IowaLiquorSales.csv')

# Conversión de columnas a tipos numéricos
data['State Bottle Cost'] = pd.to_numeric(data['State Bottle Cost'].str.replace('$', ''), errors='coerce')
data['State Bottle Retail'] = pd.to_numeric(data['State Bottle Retail'].str.replace('$', ''), errors='coerce')
data['Sale (Dollars)'] = pd.to_numeric(data['Sale (Dollars)'].str.replace('$', ''), errors='coerce')

# Visualización de histograma de 'Bottles Sold'
plt.figure(figsize=(12, 6))
plt.hist(data['Bottles Sold'], bins=20, color='skyblue')
plt.xlabel('Cantidad de Botellas Vendidas')
plt.ylabel('Frecuencia')
plt.title('Distribución de Botellas Vendidas')
plt.grid(axis='y', alpha=0.75)
plt.show()

