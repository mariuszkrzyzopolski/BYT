from main import db
from models.Plant import Plant
from models.User import User
import atexit
from flask_mail import Mail, Message
from apscheduler.schedulers.background import BackgroundScheduler


def add_plant_to_account(plant_id, u_name):
    user = User.query.filter_by(username=u_name).first()
    plant = Plant.query.filter_by(id=plant_id).first()
    plant.ownership = user.id
    db.session.commit()


def send_mail(message, subject, recipient):
    with app.app_context():
        mail = Mail(app)
        msg = Message(body=message,
                      subject=subject,
                      sender="mucholowka@mail.com",
                      recipients=[recipient])
        mail.send(msg)


def schedule_mail(mail_app, context):
    global app
    app = mail_app
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=send_mail, kwargs=context, trigger="interval", minutes=5)
    scheduler.start()

    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())
