from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, BooleanField
from wtforms.validators import DataRequired, Length


class RegistForm(FlaskForm):
    number = StringField(
        'number',
        validators=[
            DataRequired('numberは必須です。'),
            Length(1, 4, '4文字以内で入力してください。'),
        ],
    )
    nickname = StringField(
        'nickname',
        validators=[
            DataRequired('nicknameは必須です。'),
            Length(1, 20, '20文字以内で入力してください。'),
        ],
    )
    p_flag = BooleanField('p_flag')
    
    submit = SubmitField("新規登録")
    
class UpdateForm(RegistForm):
    submit = SubmitField("更新")
    

class AllUpdateForm(FlaskForm):
    all = FieldList(FormField(RegistForm),min_entries=10)
    submit = SubmitField("全て更新")