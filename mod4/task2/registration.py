from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import InputRequired, Email, NumberRange, ValidationError

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False


def number_length(min_length: int, max_length: int, message: str = None):
    def _number_length(form: FlaskForm, field: IntegerField):
        if field.data is not None:
            if not (min_length <= len(str(field.data)) <= max_length):
                if message is None:
                    raise ValidationError(f'Field must be between {min_length} and {max_length} characters long.')
                else:
                    raise ValidationError(message)
    return _number_length


class NumberLength:
    def __init__(self, min_length: int, max_length: int, message: str = None):
        self.min_length = min_length
        self.max_length = max_length
        self.message = message

    def __call__(self, form: FlaskForm, field: IntegerField):
        if field.data is not None:
            if not (self.min_length <= len(str(field.data)) <= self.max_length):
                if self.message is None:
                    self.message = f'Field must be between {self.min_length} and {self.max_length} characters long.'
                raise ValidationError(self.message)

class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(message="Email is required"), Email()])
    phone = IntegerField(validators=[InputRequired(), number_length(10, 11, message="Phone number must be between 10 "
                                                                                    "and 11 digits long.")])
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[InputRequired()])
    comment = StringField()


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f"Successfully registered user {email} with phone +7{phone}"

    return f"Invalid input, {form.errors}", 400


if __name__ == "__main__":
    app.run(debug=True)
