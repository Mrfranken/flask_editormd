from wtforms import Form, StringField, PasswordField, TextAreaField, TextField
from wtforms.validators import Length, NumberRange, DataRequired, Email, ValidationError, EqualTo


class MarkDownForm(Form):
    title = StringField(
        validators=[DataRequired(message='title can not be empty'),
                    Length(min=5, max=30, message='title length must be in range of 4 to 30')]
    )

    editor_content = TextAreaField(
        validators=[DataRequired(message='content can not be empty'),
                    Length(max=10000)]
    )
