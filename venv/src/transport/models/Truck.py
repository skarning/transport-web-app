from transport import db


class Truck(db.Model):
    __tablename__ = "Trucks"
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.Integer, unique=False, nullable=False)
    type = db.Column(db.String(40), unique=False, nullable=False)
    missions = db.relationship("Mission", backref="Trucks", lazy=True)
