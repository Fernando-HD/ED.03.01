from flask import Flask
from .contacts import contacts
from .db import init_db

app = Flask(__name__)

init_db(app)

app.register_blueprint(contacts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
