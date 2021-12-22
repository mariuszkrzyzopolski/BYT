import atexit
import sys

from flask_mail import Mail, Message
from apscheduler.schedulers.background import BackgroundScheduler


def send_mail(app):
    mail = Mail(app)
    msg = Message("Sample",
                  sender="warhir@gmail.com",
                  recipients=["m92686260@gmail.com"])
    print(app.config['MAIL_USERNAME'], file=sys.stderr)
    mail.send(msg)


def schedule_mail(app):
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=send_mail(app), trigger="interval", minutes=5)
    scheduler.start()

    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())
