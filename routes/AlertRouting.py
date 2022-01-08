from flask import url_for, render_template, request, redirect, session

from main import app
from controllers.UserController import *
from controllers.AlertController import *


@app.route("/alert", methods=['GET', 'POST'])
def alert():
    if session.get("username") is not None:
        if request.method == 'GET':
            return render_template('addNotification.html', plants=User.query.filter_by(username=session.
                                                                                       get('username')).first().plants)
        else:
            email = User.query.filter_by(username=session.get('username')).first().email
            context = {"recipient": email, "subject": "Przypomnienie z aplikacji Muchołówka",
                       "message": session.get("username") + " " + choose_alert_kind(request.form['kind']) + " " +
                                  request.form['plant']}
            schedule_mail(app, context, request.form['frequency'])
            return redirect(url_for("start"))
    else:
        return redirect(url_for("login"))
