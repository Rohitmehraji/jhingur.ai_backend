import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

def test_register(client: TestClient, db_session: Session):
    response = client.post("/auth/register", json={"email": "test@example.com", "password": "password"})
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"

def test_login(client: TestClient, db_session: Session):
    client.post("/auth/register", json={"email": "test@example.com", "password": "password"})
    response = client.post("/auth/login", data={"username": "test@example.com", "password": "password"})
    assert response.status_code == 200
    assert "access_token" in response.json()
