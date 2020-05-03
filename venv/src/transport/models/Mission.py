from transport import db
from transport.models.Truck import Truck
from transport.models.TransportationWorker import TransportationWorker


class Mission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    postal_code = db.Column(db.String(4), unique=False, nullable=False)
    address = db.Column(db.String(40), unique=False, nullable=False)
    date = db.Column(db.Date, unique=False, nullable=False)

    """Mission Relationships"""
    truck_id = db.Column(
        db.Integer, db.ForeignKey("Trucks.id"), nullable=True)
    transportation_worker_id = db.Column(
        db.Integer, db.ForeignKey("TransportationWorkers.id"), nullable=True)

    def __init__(self, postal_code, address,
                 date, truck, transportation_worker):
        self.postal_code = postal_code
        self.address = address
        self.date = date

        """
        Add current mission to respective
        trucks and transportation workers
        """
        truck.missions.append(self)
        transportation_worker.missions.append(self)
