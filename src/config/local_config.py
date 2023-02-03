from base_config import BaseConfig


class LocalConfig(BaseConfig):
    mongodb_url = super.mongodb_base_url + 'spendManagerPOCTestDB'
