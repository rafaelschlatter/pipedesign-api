import os


class Config():
    DEBUG = False
    TESTING = False
    BLOB_KEY1 = os.environ["BLOB_KEY1"]
    STORAGE_ACC_NAME = os.environ["STORAGE_ACC_NAME"]
    CONTAINER_NAME_DATA = os.environ["CONTAINER_NAME_DATA"]
    CONTAINER_NAME_MODELS = os.environ["CONTAINER_NAME_MODELS"]


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
