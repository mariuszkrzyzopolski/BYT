from main import app, db
from routes import blueprint

app.register_blueprint(blueprint)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
