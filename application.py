from flask import Flask
from src.apis import api
from src.config import config_by_name


def create_app(config_name="dev"):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    api.init_app(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
