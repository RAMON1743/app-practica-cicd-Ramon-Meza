from flask import Flask, render_template
import redis

app = Flask(__name__)

# Conectar a Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route('/')
def index():
    counter = redis_client.get('counter')
    counter = int(counter) if counter else 0
    return render_template('index.html', counter=counter)

@app.route('/increment', methods=['GET'])
def increment_counter():
    counter = redis_client.incr('counter')
    return render_template('index.html', counter=counter)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
