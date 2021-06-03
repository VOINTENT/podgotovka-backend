from src.extra.utils.config import ConfigUtils

TITLE_API = ConfigUtils.env('PODGOTOVKA_API_TITLE', str)
DESCRIPTION_API = ConfigUtils.env('PODGOTOVKA_API_DESCRIPTION', str)
VERSION_API = ConfigUtils.env('PODGOTOVKA_API_VERSION', str)
DEBUG = ConfigUtils.env('PODGOTOVKA_DEBUG', bool)
