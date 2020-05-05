from transport import db


class Truck(db.Model):
    __tablename__ = "Trucks"
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(40), unique=False, nullable=False)
    type = db.Column(db.String(40), unique=False, nullable=False)
    missions = db.relationship("Mission", back_populates="truck", lazy=True)

    def __init__(self, brand, type):
        self.brand = brand
        self.type = type

    def __repr__(self):
        return ("Number: {0}, {1}, {2}".format(
            self.id, self.brand, self.type
        ))
