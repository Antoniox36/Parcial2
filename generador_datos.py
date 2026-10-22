import os
import pandas as pd
import numpy as np

FILE_PATH = "inventario.csv"

def generar_o_cargar_inventario():
    if not os.path.exists(FILE_PATH):
        np.random.seed(42)
        sucursales = ["San Salvador", "Santa Ana", "San Miguel", "La Libertad", "Sonsonate"]
        categorias = ["Electrónica", "Ropa", "Hogar", "Alimentos", "Juguetería"]
        
        data = {
            "ID_Producto": [f"PROD-{100+i}" for i in range(100)],
            "Sucursal": np.random.choice(sucursales, 100),
            "Categoria": np.random.choice(categorias, 100),
            "Stock_Disponible": np.random.randint(5, 150, 100),
            "Precio_Unitario": np.round(np.random.uniform(5.0, 300.0, 100), 2)
        }
        df = pd.DataFrame(data)
        df.to_csv(FILE_PATH, index=False)
        print("inventario.csv generado con éxito.")
    else:
        df = pd.read_csv(FILE_PATH)
    return df

def obtener_resumen_estadistico(df):
    buffer = []
    buffer.append("=== ESTRUCTURA DE DATOS (df.shape) ===")
    buffer.append(f"Filas: {df.shape[0]} | Columnas: {df.shape[1]}\n")
    
    buffer.append("=== TIPOS DE DATOS (df.dtypes) ===")
    buffer.append(str(df.dtypes) + "\n")
    
    buffer.append("=== ESTADÍSTICAS DESCRIPTIVAS (df.describe()) ===")
    buffer.append(str(df.describe()) + "\n")

    buffer.append("=== CONTEO POR SUCURSAL ===")
    buffer.append(str(df['Sucursal'].value_counts()))

    return "\n".join(buffer)

if __name__ == "__main__":
    df_test = generar_o_cargar_inventario()
    print(obtener_resumen_estadistico(df_test))