from src.extra.utils.config import ConfigUtils

FILES_LINK = ConfigUtils.env('PODGOTOVKA_FILES_LINK', str)
SECRET_KEY = ConfigUtils.env('PODGOTOVKA_SECRET_KEY', str)
ENCRYPT_ALGORITHM = ConfigUtils.env('PODGOTOVKA_ENCRYPT_ALGORITHM', str)
