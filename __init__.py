from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.from_object('config')
mongo = PyMongo(app)
bd=0


from app import views