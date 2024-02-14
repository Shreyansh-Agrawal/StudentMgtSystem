from app import create_app
from fastapi.testclient import TestClient

app = create_app()
client = TestClient(app) 


def test_return_health_check():
    response = client.get('health-check')
    print(response)
    assert response.status_code == 200
    assert response.json() == {'status': 'Healthy'}
