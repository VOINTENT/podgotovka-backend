from starlette.testclient import TestClient


def test_test(client: TestClient, truncate):
    response = client.get('/core/v1/test')
    assert response.status_code == 200
    assert response.json() is True
