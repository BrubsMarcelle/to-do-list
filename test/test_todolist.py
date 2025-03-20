def test_create_todo(client):
    response = client.post("/v1/todos/", json={"title": "Test", "description": "Test desc"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test"