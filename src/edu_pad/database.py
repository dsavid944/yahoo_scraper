import pandas as pd
import sqlite3
import os
from datetime import datetime

class DataBase:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.rutadb = os.path.join(base_dir, "static", "db", "yahoo_data.db")

    # Funcion para guarda la informacion
    def guardar_df(self, df, nombre_tabla="yahoo_scraper"):
        try:
            conn = sqlite3.connect(self.rutadb)
            df = df.copy()
            hoy = datetime.today().strftime("%Y-%m-%d")
            df["fecha_create"] = hoy
            df["fecha_update"] = hoy
            df.to_sql(nombre_tabla, conn, if_exists="replace", index=False)
            print(f"✅ Guardado en base de datos ({df.shape[0]} registros)")
        except Exception as e:
            print(f"❌ Error guardando en BD: {e}")

    # Funcion para Obtener los datos la Bd
    def obtener_datos(self, nombre_tabla="yahoo_scraper"):
        try:
            conn = sqlite3.connect(self.rutadb)
            df = pd.read_sql(f"SELECT * FROM {nombre_tabla}", conn)
            print(f"✅ Cargado desde BD ({df.shape[0]} registros)")
            return df
        except Exception as e:
            print(f"❌ Error leyendo de BD: {e}")
            return pd.DataFrame()