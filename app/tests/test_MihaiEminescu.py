import pytest
from MihaiEminescu import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Mihai Eminescu' in response.data

def test_biografie(client):
    response = client.get('/eminescu/biografie')
    assert response.status_code == 200
    assert b'Mihai Eminescu' in response.data or b'nascut' in response.data.lower()

def test_opere(client):
    response = client.get('/eminescu/opere')
    assert response.status_code == 200
    assert b'Luceafarul' in response.data or b'opere' in response.data.lower()

def test_citat(client):
    response = client.get('/eminescu/citat')
    assert response.status_code == 200
    assert b'Eminescu' in response.data or b'citat' in response.data.lower()
