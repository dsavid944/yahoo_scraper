import pandas as pd
import requests
from bs4 import BeautifulSoup

class YahooScraper:
    def __init__(self):
        self.url = "https://finance.yahoo.com/markets/private-companies/highest-valuation/"
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def obtener_datos(self):
        try:
            resp = requests.get(self.url, headers=self.headers)
            if resp.status_code != 200:
                print("La página no respondió correctamente.")
                return pd.DataFrame()

            soup = BeautifulSoup(resp.text, "html.parser")

            # Buscar la tabla
            table = soup.find("table")
            if not table:
                print("No se encontró la tabla.")
                return pd.DataFrame()

            headers = [th.text.strip() for th in table.find_all("th")]
            rows = []
            for tr in table.find_all("tr")[1:]:
                cells = [td.text.strip() for td in tr.find_all("td")]
                if len(cells) == len(headers):
                    rows.append(cells)

            df = pd.DataFrame(rows, columns=headers)
            print("✅ Datos obtenidos correctamente.")
            return df

        except Exception as e:
            print(f"❌ Error durante el scraping: {e}")
            return pd.DataFrame()