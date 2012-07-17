from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://angelo:ciaobella@localhost/trip2'
db = SQLAlchemy(app)
