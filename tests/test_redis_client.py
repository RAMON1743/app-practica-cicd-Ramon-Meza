import pytest
from redis_client import get_redis_client

@pytest.fixture
def redis_client():
    return get_redis_client()

def test_redis_connection(redis_client):
    # Verificar que Redis está disponible
    assert redis_client.ping()
