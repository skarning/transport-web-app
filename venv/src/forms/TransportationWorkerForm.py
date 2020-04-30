from wtforms import StringField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email
from wtforms.fields.html5 import EmailField
from flask_wtf import FlaskForm


class TransportationWorkerForm(FlaskForm):

    full_name = StringField("Full name", [
        DataRequired(), Length(min=3, max=40)
    ])
    birthday = DateField("Birthday", [
        DataRequired()
    ])
    job_title = StringField("Job title", [
        DataRequired(), Length(min=2)
    ])
    email = EmailField("E-mail", [
        Email(), DataRequired()
    ])
    phone_number = StringField("Phone Number", [DataRequired()])
