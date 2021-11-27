from flask import Flask, url_for, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/login", methods=['GET', 'POST'])
def login():
    url_for('static', filename='style.css')
    if request.method == 'GET':
        return render_template('logowanie.html')
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


@app.route('/register/', methods=['GET', 'POST'])
def register():
    """Register Form"""
    if request.method == 'POST':
        new_user = User(
            username=request.form['username'],
            password=request.form['password'])
        db.session.add(new_user)
        db.session.commit()
        return render_template('login.html')
    return render_template('register.html')


@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)


@app.route("/logout")
def logout():
    """Logout Form"""
    session['logged_in'] = False
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    db = SQLAlchemy(app)
    app.debug = True
    db.create_all()
    app.run()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))

    def __init__(self, username, password):
        self.username = username
        self.password = password
