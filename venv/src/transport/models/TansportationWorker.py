from transport-as-web-app import db


class TransportationWorker(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(40), unique=False, nullable=False)
    birthday = db.Column.String(10)
    job_title = db.Column.String(60)
    email = db.Column(db.String(60)), unique=True, nullable=False)
    phone_number = db.Columns(db.String(12))
