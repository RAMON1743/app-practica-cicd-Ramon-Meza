import pytest
from app import increment_counter, create_redis_client

@pytest.fixture
def redis_client():
    client = create_redis_client()
    yield client
    client.flushdb()  # Limpiar la base de datos después de cada prueba

def test_increment_counter(redis_client):
    # Asegurarse de que el contador se incremente correctamente
    initial_value = redis_client.get('counter')
    if initial_value is None:
        initial_value = 0
    assert increment_counter(redis_client) == initial_value + 1
