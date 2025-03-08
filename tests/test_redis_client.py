import pytest
from app.redis_client import get_redis_client  # Cambiar a la ruta correcta
from app import increment_counter

@pytest.fixture
def redis_client():
    client = get_redis_client()  # Usar get_redis_client
    yield client
    client.flushdb()  # Limpiar la base de datos después de cada prueba

def test_increment_counter(redis_client):
    # Asegurarse de que el contador se incremente correctamente
    initial_value = redis_client.get('counter')
    if initial_value is None:
        initial_value = 0
    else:
        initial_value = int(initial_value)  # Convertir a entero

    # Llamar a increment_counter
    result = increment_counter(redis_client)

    # Verificar que el contador haya sido incrementado
    assert result == initial_value + 1
    # También verificamos que el valor en Redis haya sido actualizado
    assert redis_client.get('counter') == str(initial_value + 1).encode()
