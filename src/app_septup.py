from flask import Flask
from flask_cors import CORS
import logging
from datetime import timedelta

class Application:

    app = Flask(__name__)
    CORS(app)
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.secret_key = 'secret-language-flask'
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)