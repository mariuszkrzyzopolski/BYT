from flask import Flask, url_for, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))

    def __init__(self, username, password):
        self.username = username
        self.password = password

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['username']
        password = request.form['password']
        try:
            data = User.query.filter_by(username=name, password=password).first()
            if data is not None:
                session['logged_in'] = True
                return redirect(url_for('home'))
            else:
                return "Don't Login"
        except:
            return "Don't Login"


@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)