import pytest
import json
from application import app


class TestModel():
    def test_model_get_current_model_not_trained(self, client):
        resp = client.get("/model/current/")
        assert resp.status_code == 200
        assert resp.json["Error"] == "Model has not been trained yet. Train model first."


    def test_model_get_current_model_success(self, client):
        client.put("/model/train_current/50")
        resp = client.get("/model/current/")
        assert resp.status_code == 200
        assert resp.json["samples_used"] == "50"


    def test_model_train_current_success(self, client):
        resp = client.put("/model/train_current/50")
        assert resp.status_code == 200
        assert resp.json["training_result"] == "Success"


    def test_model_train_current_with_invalid_parameter(self, client):
        resp = client.put("/model/train_current/f")
        assert resp.status_code == 500
