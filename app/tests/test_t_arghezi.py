import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import pytest
from app.t_arghezi import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Tudor Arghezi' in response.data  # verificăm dacă apare numele

def test_biografie(client):
    response = client.get('/biografie')
    assert response.status_code == 200
    assert b'Arghezi' in response.data

def test_opere(client):
    response = client.get('/opere')
    assert response.status_code == 200
    assert b'Flori de mucigai' in response.data  # titlul operei testate

def test_citat(client):
    response = client.get('/citat')
    assert response.status_code == 200
    assert b'stelele' in response.data  # cuvânt din citatul testat
import pytest
from app.t_arghezi import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Tudor Arghezi' in response.data  # verificăm dacă apare numele

def test_biografie(client):
    response = client.get('/biografie')
    assert response.status_code == 200
    assert b'Arghezi' in response.data

def test_opere(client):
    response = client.get('/opere')
    assert response.status_code == 200
    assert b'Flori de mucigai' in response.data  # titlul operei testate

def test_citat(client):
    response = client.get('/citat')
    assert response.status_code == 200
    assert b'stelele' in response.data  # cuvânt din citatul testat
