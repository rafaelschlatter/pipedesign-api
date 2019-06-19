import json
from tests.helper_functions import HelperFunctions


class TestPrediction():
    def test_prediction_predict_current_without_json(self, client):
        resp = client.post("/prediction/predict_current/")
        assert resp.status_code == 400
        assert resp.json["message"] == "Input payload validation failed"


    def test_prediction_predict_current_with_json(self, client):
        pipedesign_json = HelperFunctions._load_json()
        resp = client.post("/prediction/predict_current/", json=pipedesign_json)
        assert resp.status_code == 200
        assert resp.json["prediction"] == "Viable"
        assert resp.json["confidence"] == "0.0"
        assert resp.json["label"] == "1"
        assert resp.json["pipedesign_id"] == "0a234fea9682454facab730c0a7f83f0"


    def test_prediction_predict_pickled_without_json(self, client):
        resp = client.post("prediction/predict_pickled/")
        assert resp.status_code == 400
        assert resp.json["message"] == "Input payload validation failed"


    def test_prediction_predict_pickled_with_json(self, client):
        pipedesign_json = HelperFunctions._load_json()
        resp = client.post("prediction/predict_pickled/", json=pipedesign_json)
        assert resp.status_code == 200
        assert resp.json["prediction"] == "Viable"
        assert resp.json["confidence"] == "0.00985992289985627"
        assert resp.json["label"] == "1"
        assert resp.json["pipedesign_id"] == "0a234fea9682454facab730c0a7f83f0"
