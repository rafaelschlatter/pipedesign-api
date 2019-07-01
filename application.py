from flask import Flask
from src import create_app

app = create_app("prod")
