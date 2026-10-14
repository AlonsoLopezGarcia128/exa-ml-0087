# Alonso Lopez Garcia NC = 0087
import sys
import os
import io
import pandas as pd

# Permitir importar dicc_0087.py desde la subcarpeta hermana 'datos-de-entrada-ml-0087'
ruta_datos = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'datos-de-entrada-ml-0087'))
if ruta_datos not in sys.path:
    sys.path.append(ruta_datos)

import dicc_0087

encabezado_pie = "Alonso Lopez Garcia Machine Learning pandas, NC 0087"
print(encabezado_pie)

# Variable para almacenar las salidas y guardarlas en el archivo .md
contenido_md = []
contenido_md.append(f"# Reporte de Análisis de Datos - Pandas\n\n`{encabezado_pie}`\n")

def registrar(titulo, contenido):
    """Muestra el resultado en terminal y lo formatea para el archivo Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)
    contenido_md.append(f"## {titulo}\n```text\n{contenido}\n```\n")

# 1. Convertir diccionario a DataFrame usando el módulo importado
df = pd.DataFrame(dicc_0087.datos_videojuegos)
registrar("1. DataFrame Convertido", df)

# 2. Información Estructural
registrar("2.1 Primeras Filas (head)", df.head(2))
registrar("2.2 Últimas Filas (tail)", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# Capturar salida de df.info()
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info)", buffer.getvalue())

# 3. Estadísticas Generales de una Columna Numérica (Precio)
registrar("3. Estadísticas Generales de la Columna 'Precio'", df['Precio'].describe())

# 4. Ordenar Ascendente por Precio
df_asc_precio = df.sort_values(by="Precio", ascending=True)
registrar("4. Ordenar Ascendente por Precio", df_asc_precio)

# 5. Ordenar Descendente por Precio
df_desc_precio = df.sort_values(by="Precio", ascending=False)
registrar("5. Ordenar Descendente por Precio", df_desc_precio)

# 6. Guardar el archivo resultados-ml-0087.md dentro de la carpeta resultados-ml-0087
carpeta_resultados = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resultados-ml-0087'))
os.makedirs(carpeta_resultados, exist_ok=True)
ruta_archivo_md = os.path.join(carpeta_resultados, "resultados-ml-0087.md")

contenido_md.append(f"`{encabezado_pie}`")

with open(ruta_archivo_md, "w", encoding="utf-8") as f:
    f.write("\n".join(contenido_md))

print(f"\n[ÉXITO] Archivo generado correctamente en: {ruta_archivo_md}")

print(encabezado_pie)

print("Alonso Lopez Garcia NC = 0087")