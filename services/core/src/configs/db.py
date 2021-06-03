from src.extra.utils.config import ConfigUtils

DB_HOST = ConfigUtils.env('PODGOTOVKA_DB_HOST', str)
DB_PORT = ConfigUtils.env('PODGOTOVKA_DB_PORT', int)
DB_USER = ConfigUtils.env('PODGOTOVKA_DB_USER', str)
DB_PASSWORD = ConfigUtils.env('PODGOTOVKA_DB_PASSWORD', str)
PRIMARY_DB_NAME = ConfigUtils.env('PODGOTOVKA_PRIMARY_DB_NAME', str)
LOGS_DB_NAME = ConfigUtils.env('PODGOTOVKA_LOGS_DB_NAME', str)
