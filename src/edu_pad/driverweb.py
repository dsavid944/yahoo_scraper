from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time
class YahooSeleniumScraper:
    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(options=options)
        self.url = "https://finance.yahoo.com/markets/private-companies/highest-valuation/"

    def obtener_datos(self):
        self.driver.get(self.url)
        time.sleep(3)  # Tiempop de Esperar a que cargue

        try:
            table = self.driver.find_element(By.TAG_NAME, 'table')
            headers = [th.text.strip() for th in table.find_elements(By.TAG_NAME, 'th')]
            rows = []

            for tr in table.find_elements(By.TAG_NAME, 'tr')[1:]:
                cells = [td.text.strip() for td in tr.find_elements(By.TAG_NAME, 'td')]
                if len(cells) == len(headers):
                    rows.append(cells)

            df = pd.DataFrame(rows, columns=headers)
            print("✅ Datos capturados con Selenium")
            return df
        except Exception as e:
            print(f"❌ Error en Selenium scraping: {e}")
            return pd.DataFrame()
        finally:
            self.driver.quit()
