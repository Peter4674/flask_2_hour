from flask import Blueprint, render_template, request, flash

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
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("name")
        pass1 = request.form.get("password1")
        pass2 = request.get.form("password2")
        if len(email) < 4:
            flash("Email must be longer than 4 characters", category = "error")
        elif len(firstName) < 2:
            flash("Name must be longer than 1 character", category = "error")
        elif pass1 != pass2:
            flash("Your passwords must match", category = "error")
        elif len(pass1) < 7:
            flash("Your password must be longer than 6 characters", category = "error")
        else:
            flash("account created", category = "success")
            

    return render_template("sign_up.html")       