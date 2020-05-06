from wtforms import StringField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm


class TruckForm(FlaskForm):
    brand = StringField("Brand", [DataRequired(), Length(max=40)])
    type = StringField("Type", [DataRequired(), Length(max=40)])
    registration_number = StringField("Registration-number",
                                      [DataRequired(), Length(min=8, max=8)])
