from dataweb import YahooScraper
from database import DataBase

def main():
    scraper = YahooScraper()
    db = DataBase()

    df = scraper.obtener_datos()
    if not df.empty:
        db.guardar_df(df)
        df_db = db.obtener_datos()
        df_db.to_csv("src/edu_pad/static/csv/yahoo_data.csv", index=False)
        print("✅ Proceso completado")
    else:
        print("❌ No se procesaron datos")

if __name__ == "__main__":
    main()