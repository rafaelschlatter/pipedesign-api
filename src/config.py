import os
import logging


class Config:
    BLOB_KEY1 = os.environ["BLOB_KEY1"]
    STORAGE_ACC_NAME = os.environ["STORAGE_ACC_NAME"]
    CONTAINER_NAME_DATA = os.environ["CONTAINER_NAME_DATA"]
    CONTAINER_NAME_MODELS = os.environ["CONTAINER_NAME_MODELS"]
    APPINSIGHTS_INSTRUMENTATIONKEY = os.environ["APPINSIGHTS_INSTRUMENTATIONKEY"]


class DevelopmentConfig(Config):
    ENV = "dev"
    DEBUG = True
    TESTING = False
    LOGGING_LEVEL = logging.DEBUG


class TestingConfig(Config):
    ENV = "test"
    DEBUG = True
    TESTING = True
    LOGGING_LEVEL = logging.INFO


class ProductionConfig(Config):
    ENV = "prod"
    DEBUG = False
    TESTING = False
    LOGGING_LEVEL = logging.ERROR


config_by_name = dict(dev=DevelopmentConfig, test=TestingConfig, prod=ProductionConfig)
