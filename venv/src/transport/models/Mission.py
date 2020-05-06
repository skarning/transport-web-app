""" Model of a Mission.

This module creates a SQLAlchemy model. The model models a mission.
The model defines the columns and the relationships that the mission has.

    Typical Usage example:

    Mission("1734", "sunny-road 97", "11-07-1997")
"""
from transport import db


class Mission(db.Model):
    """
    Attributes
        id: An Intgeer that defines the primary key of the table
        postal_code: A String of 4 character that defines the postal code
        address: A String that defines the delivery address
        date: A string that defines the delivery date of the mission
        truck_id: An Integer that is the foreign key for a truck
        transportation_worker_id: An integer that is the
        foreign key for a transportation_worker
        truck: A Truck object that defines the truck to be used
        in the mission
        transportation_worker: A TransportationWorker object that defines
        what transportation worker that is assigned to mission
    """
    id = db.Column(db.Integer, primary_key=True)
    postal_code = db.Column(db.String(4), unique=False, nullable=False)
    address = db.Column(db.String(40), unique=False, nullable=False)
    date = db.Column(db.Date, unique=False, nullable=False)

    # Mission Foreign keys
    truck_id = db.Column(
        db.Integer, db.ForeignKey("Trucks.id"), nullable=True)
    transportation_worker_id = db.Column(
        db.Integer, db.ForeignKey("TransportationWorkers.id"), nullable=True)

    # Holds object defined in relationship
    truck = db.relationship("Truck", back_populates="missions")
    transportation_worker = db.relationship(
        "TransportationWorker", back_populates="missions"
    )

    """Contructs an object of type Mission"""
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
