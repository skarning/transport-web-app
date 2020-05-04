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
        "Mission", back_populates="transportation_worker", lazy=True)

    def __init__(self, full_name, birthday,
                 email, job_title, phone_number):
        self.full_name = full_name
        self.birthday = birthday
        self.job_title = job_title
        self.email = email
        self.phone_number = phone_number

    def __repr__(self):
        return ("{0}, {1}, {2}".format(
            self.full_name, self.email, self.phone_number
        ))
