class SingletonConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonConfig, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            # Inicializa los parámetros de configuración aquí
            self.database_url = "localhost:5432/mydatabase"
            self.api_key = "YOUR_API_KEY"
            self.debug_mode = True
            self._initialized = True

    def show_config(self):
        return {
            "database_url": self.database_url,
            "api_key": self.api_key,
            "debug_mode": self.debug_mode
        }

config1 = SingletonConfig()
config2 = SingletonConfig()

# Ambas variables apuntan a la misma instancia
print(config1 is config2)  # Output: True

# Mostrar la configuración
print(config1.show_config())  
