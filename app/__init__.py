from flask import Flask ## import Flask

app = Flask(__name__)

from app.controllers import *