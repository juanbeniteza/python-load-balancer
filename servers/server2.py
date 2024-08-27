import time
import random
from flask import Flask

app = Flask(__name__)


@app.route('/<path:path>', methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def process(path):
    wait = random.randint(1, 10)

    time.sleep(wait)

    return f"Server 2, request to path {path} waited for {wait} secs."


if __name__ == "__main__":
    app.run(host='localhost', port=5002)