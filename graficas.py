from statistics import LinearRegression
import pandas as pd
from sklearn.model_selection import train_test_split
# Lee el archivo CSV
data = pd.read_csv('IowaLiquorSales.csv')
import matplotlib.pyplot as plt
import numpy as np

""""
#------------------------------------------------------------------------------
#HISTOGRAMA: Bottles Sold y Volume Sold (Liters)

# columnas numéricas para visualizar
columns_to_plot = ['Bottles Sold', 'Volume Sold (Liters)']

# Configuracion del tamaño de la figura
plt.figure(figsize=(12, 6))

# Dibujar histogramas para las columnas seleccionadas
for i, column in enumerate(columns_to_plot, 1):
    plt.subplot(1, len(columns_to_plot), i)
    plt.hist(data[column], bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Histograma de {column}')
    plt.xlabel(column)
    plt.ylabel('Frecuencia')

# Ajuste del diseño de la figura y muestra los histogramas
plt.tight_layout()
plt.show()

#------------------------------------------------------------------------------
"""


"""
#------------------------------------------------------------------------------
#DIAGRAMA DE DISPERCION:  visualizar la tendencia entre las variables Bottles Sold y Sale (Dollars)

# Convertir la columna 'Sale (Dollars)' a valores numéricos
data['Sale (Dollars)'] = data['Sale (Dollars)'].str.replace('$', '').astype(float)

# Configurar el tamaño de la figura
plt.figure(figsize=(8, 6))

# Crear un diagrama de dispersión para Bottles Sold y Sale (Dollars)
plt.scatter(data['Bottles Sold'], data['Sale (Dollars)'], color='purple', alpha=0.5)
plt.title('Diagrama de Dispersión: Bottles Sold vs. Sale (Dollars)')
plt.xlabel('Bottles Sold')
plt.ylabel('Sale (Dollars')

# Calcular la línea de regresión
m, b = np.polyfit(data['Bottles Sold'], data['Sale (Dollars)'], 1)
plt.plot(data['Bottles Sold'], m * data['Bottles Sold'] + b, color='red')

# Mostrar el diagrama de dispersión con la línea de regresión
plt.show()
#------------------------------------------------------------------------------
"""

"""
#------------------------------------------------------------------------------
# Selecciona la columna categórica que deseas analizar
categorical_column = 'City'

# Calcula la frecuencia de cada categoría en la columna seleccionada
category_counts = data[categorical_column].value_counts()

# Configura el tamaño de la figura
plt.figure(figsize=(12, 6))

# Crea un gráfico de barras para visualizar la distribución de categorías
plt.bar(category_counts.index, category_counts.values, color='skyblue')

# Añade etiquetas y título al gráfico
plt.xlabel(categorical_column)
plt.ylabel('Frecuencia')
plt.title(f'Distribución de {categorical_column}')

# Ajusta el diseño del gráfico y muestra el gráfico de barras
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
##------------------------------------------------------------------------------
"""
