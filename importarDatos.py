"""""
#------------------------------------------------------
import pandas as pd

# Lee el archivo CSV
data = pd.read_csv('IowaLiquorSales.csv')

# Muestra el recuento de registros
print("Recuento de registros en la base de datos:")
print(len(data))

# Información de cada columna
print("\nInformación de las columnas:")
print(data.info())

# Estadísticas descriptivas para columnas numéricas
print("\nEstadísticas descriptivas básicas:")
print(data.describe())

# Identifica valores nulos
print("\nValores nulos por columna:")
print(data.isnull().sum())
# Muestra el contenido del dataset
#print(data)

columnas = data.columns
print("Nombres de las columnas:")
for col in columnas:
    print(col)
    
# Selecciona algunas columnas numéricas para visualizar
columns_to_plot = ['Bottles Sold', 'Volume Sold (Liters)']
#------------------------------------------------------
"""