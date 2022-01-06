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


def choose_alert_kind(form):
    if form == "Podlewanie":
        return "Podlej roślinę"
    if form == "Nawożenie":
        return "Nawieź roślinę"


def schedule_mail(mail_app, context, frequency):
    global app
    app = mail_app
    scheduler = BackgroundScheduler()
    if frequency == "Codziennie":
        scheduler.add_job(func=send_mail, kwargs=context, trigger="interval", days=1)
    if frequency == "Tygodniowo":
        scheduler.add_job(func=send_mail, kwargs=context, trigger="interval", days=7)
    if frequency == "Miesięcznie":
        scheduler.add_job(func=send_mail, kwargs=context, trigger="interval", months=1)
    if frequency == "Kwartalnie":
        scheduler.add_job(func=send_mail, kwargs=context, trigger="interval", months=3)
    if frequency == "Rocznie":
        scheduler.add_job(func=send_mail, kwargs=context, trigger="interval", years=1)
    scheduler.start()

    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())
