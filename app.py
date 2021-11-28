from flask import Flask, url_for, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = '1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://sql11454497:RwkSDDxD8v@sql11.freemysqlhosting.net' \
                                        ':3306/sql11454497 '
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True
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
        return render_template('logowanie.html')
    else:
        app.logger.debug(request.form['loguj'])
        if request.form['loguj'] == "Zaloguj":
            name = request.form['username']
            password = request.form['password']
            data = User.query.filter_by(username=name, password=password).first()
            if data is not None:
                session['logged_in'] = True
                return redirect(url_for("hello_world"))
            else:
                return "Don't Login"
        else:
            new_user = User(
                username=request.form['username'],
                password=request.form['password'])
            db.session.add(new_user)
            db.session.commit()
            return render_template('index.html')


@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)


@app.route("/logout")
def logout():
    """Logout Form"""
    session['logged_in'] = False
    return redirect(url_for('home'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
