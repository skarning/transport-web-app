from wtforms import StringField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import DateField
from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from transport.repositories.TruckRepository import TruckRepository
from transport.repositories.TransportationWorkerRepository import TransportationWorkerRepository


class MissionForm(FlaskForm):
    truck_repos = TruckRepository()

    trans_wor_repos = TransportationWorkerRepository()

    postal_code = StringField("Postalcode", [
        DataRequired(), Length(min=4, max=4)
    ])
    address = StringField("Address", [
        DataRequired(), Length(max=40)
    ])
    date = DateField("Date", [DataRequired()])

    truck = QuerySelectField("Truck", [DataRequired()],
                             query_factory=truck_repos.get_all,
                             allow_blank=False, get_label="brand")

    transportation_worker = QuerySelectField("Transportation worker",
                                             [DataRequired()],
                                             query_factory=trans_wor_repos.get_all,
                                             allow_blank=False,
                                             get_label="full_name")
