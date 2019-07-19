import os


class Config:
    BLOB_KEY1 = os.environ["BLOB_KEY1"]
    STORAGE_ACC_NAME = os.environ["STORAGE_ACC_NAME"]
    CONTAINER_NAME_DATA = os.environ["CONTAINER_NAME_DATA"]
    CONTAINER_NAME_MODELS = os.environ["CONTAINER_NAME_MODELS"]
    APPINSIGHTS_INSTRUMENTATIONKEY = os.environ["APPINSIGHTS_INSTRUMENTATIONKEY"]


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    ENV = "testing"
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    ENV = "production"
    DEBUG = False
    TESTING = False


config_by_name = dict(dev=DevelopmentConfig, test=TestingConfig, prod=ProductionConfig)
