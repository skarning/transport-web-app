from transport import db


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
