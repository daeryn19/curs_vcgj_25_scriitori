import pytest
from n_stanescu import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Nichita St' in response.data  # verificăm dacă apare numele

def test_biografie(client):
    response = client.get('/stanescu/biografie')
    assert response.status_code == 200
    assert b'Nichita St' in response.data

def test_opere(client):
    response = client.get('/stanescu/opere')
    assert response.status_code == 200
    assert b'O viziune' in response.data

def test_citat(client):
    response = client.get('/stanescu/citat')
    assert response.status_code == 200
    assert b'A iubi' in response.data

