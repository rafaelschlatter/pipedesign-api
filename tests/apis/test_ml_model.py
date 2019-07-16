class TestMLModel:
    def test_model_get_current_model_failure(self, client):
        resp = client.get("/model/current/")
        assert resp.status_code == 404

    def test_model_get_current_model_success(self, client):
        client.put("/model/train_current/50/")
        resp = client.get("/model/current/")
        assert resp.status_code == 200
        assert resp.json["samples_used"] == "50"

    def test_model_get_pickled_model_failure(self, client):
        resp = client.get("model/pickled/")
        assert resp.status_code == 404

    def test_model_get_pickled_model_success(self, client):
        client.put("/model/activate_pickled/test_model_1_do_not_delete/")
        resp = client.get("model/pickled/")
        assert resp.status_code == 200

    def test_model_train_current_success(self, client):
        resp = client.put("/model/train_current/50/")
        assert resp.status_code == 200
        assert resp.json["training_result"] == "Successfully trained model"

    def test_model_train_current_with_invalid_parameter(self, client):
        resp = client.put("/model/train_current/f/")
        assert resp.status_code == 500

    def test_model_activate_pickled_success(self, client):
        resp = client.put("/model/activate_pickled/test_model_1_do_not_delete/")
        assert resp.status_code == 200
        assert resp.json["training_result"] == "Successfully activated model"

    def test_model_activate_pickled_failure(self, client):
        resp = client.put("/model/activate_pickled/non_existant_model_id/")
        assert resp.status_code == 500
