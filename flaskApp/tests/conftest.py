import pytest
from app import app_init, redis_db
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '../.test.env')
load_dotenv(dotenv_path)

@pytest.fixture(scope="session")
def client():
    app = app_init()
    with app.test_client() as client:
        with app.app_context():
            yield client

@pytest.fixture(scope="session", autouse=True)
def setup_db():
    assert os.getenv('MODE') == 'TESTING'
    connection = redis_db.get_redis_connection()
    assert connection.ping()
    yield 
    connection.close()
