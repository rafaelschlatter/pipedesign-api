import pytest
import json
from application import application


class TestPrediction():
    def test_prediction_predict_current_without_json(self, client):
        resp = client.post("/prediction/predict_current/")
        assert resp.status_code == 400
        assert resp.json["message"] == "Input payload validation failed"


    def test_prediction_predict_current_with_json(self, client):
        json_data = {
            "timestamp": "string",
            "design_id": "string",
            "pipe_segments": [
                {}
            ],
            "viability": {}
        }

        resp = client.post("/prediction/predict_current/", json=json_data)
        assert resp.status_code == 200
        assert resp.json["Error"] == "Model has not been trained yet. Train model first."
