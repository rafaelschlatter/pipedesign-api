import logging
from flask import Flask, request
from applicationinsights.flask.ext import AppInsights
from src.apis import api
from src.config import config_by_name


def create_app(config_name="dev"):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    api.init_app(app)
    app_insights = AppInsights(app)

    @app.after_request
    def after_request(response):
        app.logger.setLevel(logging.DEBUG)
        app.logger.critical(
            f"{response.status} - {request.remote_addr} - {request.method} - {request.scheme} - {request.full_path}"
        )
        app_insights.flush()
        return response

    return app
