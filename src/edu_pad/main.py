from dataweb import YahooScraper
from database import DataBase
import os

def main():
    scraper = YahooScraper()
    db = DataBase()

    # Obtener path absoluto
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Ruta donde se guardará el CSV
    output_csv_path = os.path.join(base_dir, "static", "csv", "yahoo_data.csv")

    df = scraper.obtener_datos()
    if not df.empty:
        db.guardar_df(df)
        df_db = db.obtener_datos()
        df_db.to_csv(output_csv_path, index=False)
        print("✅ Proceso completado")
    else:
        print("❌ No se procesaron datos")

if __name__ == "__main__":
    main()