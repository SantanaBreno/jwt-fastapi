import pytest 
from fastapi.testclient import TestClient
from app.main import app
from faker import Faker

client = TestClient(app)

faker = Faker()

name_fake = faker.name()
email_faker = faker.email()

def test_register_and_login():
    
    user_test = {     
        "email": email_faker,
        "password": "Senha teste",
        "name": name_fake
    }

    response = client.post("/user/register", json=user_test)

    assert response.status_code == 201
        
    
    login_response = client.post("/user/login", data={
        "username": user_test['email'],
        "password": user_test['password']
        })
    
    assert login_response.status_code == 200
    assert "access_token" in login_response.json()

def test_invalid_login():

    user_invalid = {
        "username": faker.email(),
        "password": "Senha invalida"
    }

    response = client.post("/user/login", data=user_invalid)

    assert response.status_code == 401
    assert "Invalid email or passsword" == response.json()["detail"]