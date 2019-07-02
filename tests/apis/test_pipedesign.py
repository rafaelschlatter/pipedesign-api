from tests.helper_functions import HelperFunctions


class TestPipedesign():
    def test_get_pipedesign_with_valid_id_success(self, client):
        resp = client.get("/pipedesign/test_blob_do_not_delete")
        assert resp.status_code == 200
        assert resp.json["design_id"] == "aef2e64b3eb94fb98ac19dd9370f2e4b"


    def test_get_pipedesign_with_invalid_id_failure(self, client):
        resp = client.get("/pipedesign/fake_id123")
        assert resp.status_code == 404
    

    def test_post_pipedesign_with_valid_json_success(self, client):
        pipedesign_json = HelperFunctions._load_json()
        resp = client.post("/pipedesign/test_blob_2_do_not_delete", json=pipedesign_json)
        assert resp.status_code == 200


    def test_post_pipedesign_with_invalid_json_failure(self, client):
        pipedesign_json = dict(key="value")
        resp = client.post("/pipedesign/test_blob_2_do_not_delete", json=pipedesign_json)
        assert resp.status_code == 400
        assert resp.json["message"] == "Input payload validation failed"
