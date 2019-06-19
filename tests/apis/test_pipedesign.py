class TestPipedesign():
    def test_get_pipedesign_with_valid_id(self, client):
        resp = client.get("/pipedesign/test_blob_do_not_delete")
        assert resp.status_code == 200
        assert resp.json["design_id"] == "aef2e64b3eb94fb98ac19dd9370f2e4b"


    def test_get_pipedesign_with_invalid_id(self, client):
        resp = client.get("/pipedesign/fake_id123")
        assert resp.status_code == 200
        assert resp.json["Error"] == "The pipedesign with the given id does not exist in Azure blob."
    