from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import atexit

app = Flask(__name__)
app.config.from_object("config.Config")
db = SQLAlchemy(app)
atexit.register(lambda: db.session.close())
