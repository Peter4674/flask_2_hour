from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route("/logout", methods=['GET', 'POST'])
def logout():
    return "<p>Logging out </p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sing_up():
    return render_template("sign_up.html")       