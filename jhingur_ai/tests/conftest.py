import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Set dummy env vars before importing the app
os.environ['TESTING'] = 'True'
os.environ['DATABASE_URL'] = 'sqlite:///./test.db'
os.environ['OPENAI_API_KEY'] = 'test'
os.environ['STRIPE_SECRET_KEY'] = 'test'
os.environ['RAZORPAY_KEY_ID'] = 'test'
os.environ['RAZORPAY_KEY_SECRET'] = 'test'
os.environ['GOOGLE_CLIENT_ID'] = 'test'
os.environ['GOOGLE_CLIENT_SECRET'] = 'test'
os.environ['GITHUB_CLIENT_ID'] = 'test'
os.environ['GITHUB_CLIENT_SECRET'] = 'test'
os.environ['SECRET_KEY'] = 'test_secret_key'
os.environ['ALGORITHM'] = 'HS256'
os.environ['ACCESS_TOKEN_EXPIRE_MINUTES'] = '30'

from app.main import app
from app.database import Base, get_db

SQLALCHEMY_DATABASE_URL = os.environ['DATABASE_URL']

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    del app.dependency_overrides[get_db]
