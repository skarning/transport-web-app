from wtforms import StringField
from wtforms.validators import DataRequired, Length, Email
from wtforms.fields.html5 import EmailField, DateField
from flask_wtf import FlaskForm


class TransportationWorkerForm(FlaskForm):

    full_name = StringField("Full name", [
        DataRequired(), Length(min=2, max=40)
    ])
    birthday = DateField("Birthday", [
        DataRequired()
    ])
    job_title = StringField("Job title", [
        DataRequired(), Length(max=60)
    ])
    email = EmailField("E-mail", [
        Email(), DataRequired(), Length(max=60)
    ])
    phone_number = StringField("Phone Number", [
        DataRequired(), Length(max=12)
    ])
