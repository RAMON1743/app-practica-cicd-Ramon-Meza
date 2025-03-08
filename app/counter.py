def increment_counter(redis_client):
    """Incrementa el valor del contador en Redis."""
    counter = redis_client.get('counter')
    if counter is None:
        counter = 0
    else:
        counter = int(counter)

    new_counter = counter + 1
    redis_client.set('counter', new_counter)  # Establecer el nuevo valor en Redis
    return new_counter
