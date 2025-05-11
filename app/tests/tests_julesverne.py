import pytest
from JulesVerne import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Jules Verne' in response.data  # verificăm dacă apare numele

def test_biografie(client):
    response = client.get('/verne/biografie')
    assert response.status_code == 200
    assert b'Jules Verne' in response.data

def test_opere(client):
    response = client.get('/verne/opere')
    assert response.status_code == 200
    assert b'20.000 de leghe' in response.data or b'Ocolul Pamantului' in response.data

def test_citat(client):
    response = client.get('/verne/citat')
    assert response.status_code == 200
    assert b"imagina" in response.data  # verificăm dacă apare fragmentul citatului
