import os
class DataBase:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.rutadb = os.path.join(base_dir, "static", "db", "yahoo_data.db")
        os.makedirs(os.path.dirname(self.rutadb), exist_ok=True)
        
        # Ruta del archivo SQLite
        self.rutadb = os.path.join(base_dir, "static", "db", "yahoo_data.db")
        os.makedirs(os.path.dirname(self.rutadb), exist_ok=True)

        # Ruta donde se guardará el CSV
        self.output_csv_path = os.path.join(base_dir, "static", "csv", "yahoo_data.csv")
        os.makedirs(os.path.dirname(self.output_csv_path), exist_ok=True)