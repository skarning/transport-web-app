from transport import db


class TransportationWorker(db.Model):
    __tablename__ = "TransportationWorkers"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(40), unique=False, nullable=False)
    birthday = db.Column(db.String(10))
    job_title = db.Column(db.String(60))
    email = db.Column(db.String(60), unique=True, nullable=False)
    phone_number = db.Column(db.String(12))
    # One to Many relationship with mission
    missions = db.relationship(
        "Mission", backref="TransportationWorkers", lazy=True)
