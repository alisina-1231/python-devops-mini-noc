from flask import Flask, Response
import prometheus_client
from prometheus_client import Counter

app = Flask(__name__)

# Define Prometheus metrics
REQUESTS = Counter('http_requests_total', 'Total HTTP Requests', ['endpoint'])

@app.route('/')
def index():
    REQUESTS.labels(endpoint='/').inc()
    return "Hello DevOps 🚀"

@app.route('/metrics')
def metrics():
    return Response(
        prometheus_client.generate_latest(),
        mimetype="text/plain; version=0.0.4; charset=utf-8"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
