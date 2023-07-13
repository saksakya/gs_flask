from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class SignUpForm(FlaskForm):
    userid = StringField(
        'UserID',
        validators=[
            DataRequired('UserIDは必須です。'),
            Length(1, 30, '30文字以内で入力してください。'),
        ],
    )
    email = StringField(
        'Mail address',
        validators=[
            DataRequired('メールアドレスは必須です。'),
            Email('形式が誤っています。'),
        ],
    )
    password = PasswordField("パスワード", validators=[DataRequired('Passwordは必須です。')])
    submit = SubmitField("新規登録")


class LoginForm(FlaskForm):
    userid = StringField('UserID',validators=[DataRequired("UserIDは必須です。")])
    password = PasswordField('パスワード', validators=[DataRequired("Passwordは必須です。")])
    submit = SubmitField('ログイン')