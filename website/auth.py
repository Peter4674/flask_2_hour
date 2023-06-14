from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Logging in</p>"

@auth.route("/logout")
def logout():
    return "<p>Logging out </p>"

@auth.route('/sign-up')
def sing_up():
    return "<p>signing up</p>"