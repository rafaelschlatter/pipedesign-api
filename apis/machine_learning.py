import os
from flask import jsonify
from flask_restplus import Resource, Namespace, fields
from ml import model
from ml import preprocessor


api = Namespace('prediction', description='Namespace holding all methods related to predictions.')

pipedesign_model = api.model(name="Pipedesign model", model=
    {
        "timestamp": fields.String(required=True),
        "design_id": fields.String(required=True),
        "pipe_segments": fields.List(cls_or_instance=fields.Raw, required=True),
        "viability": fields.Raw(required=True)
    }
)

# Having this in memory is bad, good enough for fast solution
p = preprocessor.Preprocessor()
blobs = p.download_blobs(os.environ["CONTAINER_NAME_DATA"], number_of_blobs=10)
training_data = p.create_training_data(blobs)
clf = model.Model()


@api.route("/")
class Prediction(Resource):
    @api.expect(pipedesign_model, validate=True)
    def post(self):
        """Returns a prediction on the viability of a single pipedesign."""

        prediction = clf.predict(api.payload)
        if prediction[0] == 1:
            verbal_pred = "Viable"
        else:
            verbal_pred = "Unviable"
        return jsonify({"prediction": verbal_pred, "confidence": "Not implemented yet"})
