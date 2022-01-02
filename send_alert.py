import atexit

from flask_mail import Mail, Message
from apscheduler.schedulers.background import BackgroundScheduler


def send_mail():
    with app.app_context():
        mail = Mail(app)
        msg = Message("Sample",
                      sender="mucholowka@mail.com",
                      recipients=["m92686260@gmail.com"])
        mail.send(msg)


def schedule_mail(mail_app):
    global app
    app = mail_app
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=send_mail, trigger="interval", minutes=5)
    scheduler.start()

    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())
