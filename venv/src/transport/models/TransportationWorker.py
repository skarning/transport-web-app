""" Model of a transportation worker.

This module creates a SQLAlchemy model. The model models the
transportation-worker actor in this system. The model defines
the columns and the relationships that the transportation-worker has.

    Typical Usage example:

    TransportationWorker("Lisa", "11-07-1992",
                        "Engineer", ex@mail.com "22112233")
"""
from transport import db


class TransportationWorker(db.Model):
    """
    Attributes
        __tablename__: A string that defines the SQLAlchemy table name
        id: A integer defining the primary key
        full_name: A string that defines transportation workers full name
        birthday: A string that defines transportation workers birthday
        job_title: A string that defines transportation workers job-title
        email: A string that defines the transportation workers email
        phone_number: A string that defines transportation workers phone-number
        missions: A list of missions that the transportation worker
        is scheduled for
    """
    __tablename__ = "TransportationWorkers"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(40), unique=False, nullable=False)
    birthday = db.Column(db.String(10))
    job_title = db.Column(db.String(60))
    email = db.Column(db.String(60), unique=True, nullable=False)
    phone_number = db.Column(db.String(12))

    # One to Many relationship with missions
    # back_populates for accessing related
    # transportation worker in mission
    # lazy load for auto loading missions
    missions = db.relationship(
        "Mission", back_populates="transportation_worker", lazy=True)

    def __init__(self, full_name, birthday,
                 email, job_title, phone_number):
        """ Constructs an object of type TransportationWorker"""
        self.full_name = full_name
        self.birthday = birthday
        self.job_title = job_title
        self.email = email
        self.phone_number = phone_number

    def __repr__(self):
        """Returns textual representation of object"""
        return ("{0}, {1}, {2}".format(
            self.full_name, self.email, self.phone_number
        ))
