from flask_restplus import fields
from ml_api.server import server 


ml_model_model = server.api.model(name="Machine learning model", model=
    {
        "Name": fields.String(required=True),
        "model_type": fields.String(required=True),
        "last_trained": fields.String(required=True),
        "test_accuracy": fields.String(required=True)
    }
)