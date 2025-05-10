import pytest
from ion_creanga import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Ion Creang' in response.data  # verificăm dacă apare numele

def test_biografie(client):
    response = client.get('/creanga/biografie')
    assert response.status_code == 200
    assert b'Ion Creang' in response.data

def test_opere(client):
    response = client.get('/creanga/opere')
    assert response.status_code == 200
    assert b'ul' in response.data  # căutăm un element de listă

def test_citat(client):
    response = client.get('/creanga/citat')
    assert response.status_code == 200
    assert b'blockquote' in response.data
