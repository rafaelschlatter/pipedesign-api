import pytest
import json
from application import app


class TestPrediction():
    def test_prediction_predict_current_without_json(self, client):
        resp = client.post("/prediction/predict_current/")
        assert resp.status_code == 400
        assert resp.json["message"] == "Input payload validation failed"


    def test_prediction_predict_current_with_json(self, client):
        with open("data/json/0a234fea9682454facab730c0a7f83f0.json") as f:
            json_data=json.load(f)

        resp = client.post("/prediction/predict_current/", json=json_data)
        assert resp.status_code == 200
        assert resp.json["prediction"] == "Viable"
        assert resp.json["confidence"] == "0.0"
        assert resp.json["label"] == "1"
        assert resp.json["pipedesign_id"] == "0a234fea9682454facab730c0a7f83f0"
