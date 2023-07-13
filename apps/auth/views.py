from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    request,
)
from apps.auth.form import SignUpForm, LoginForm
from apps.auth.models import User
from apps.app import db
from flask_login import login_user, logout_user

auth = Blueprint("auth", __name__, template_folder="templates", static_folder="static")

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        user = User(
            userid=form.userid.data,
            email=form.email.data,
            password=form.password.data,
        )

        if user.is_duplicate_email():
            flash('指定のメールアドレスは登録済みです。')
            return redirect(url_for("auth.signup"))

        db.session.add(user)
        db.session.commit()

        login_user(user)

        _next = request.args.get("next")
        if _next is None or not _next.startswith("/"):
            _next = url_for("student.top")
        return redirect(_next)

    return render_template("auth/signup.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(userid=form.userid.data).first()

        if user is not None:
            if user.verify_password(form.password.data):
                login_user(user)
                
                _next = request.args.get("next")
                if _next is None or not _next.startswith("/"):
                    _next = url_for("student.top")
                return redirect(_next)
            else:
                flash('Passwordが一致しません。')
        else:
            flash('入力されたUserは存在しません。')
        
    return render_template("auth/login.html", form=form)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))