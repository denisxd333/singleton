class Config:
    def __init__(self):
        # Inicializa los parámetros de configuración aquí
        self.database_url = "localhost:5432/mydatabase"
        self.api_key = "YOUR_API_KEY"
        self.debug_mode = True

    def show_config(self):
        return {
            "database_url": self.database_url,
            "api_key": self.api_key,
            "debug_mode": self.debug_mode
        }
