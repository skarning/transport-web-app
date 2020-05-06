""" Model of a Truck.

This module creates a SQLAlchemy model. The model models a truck.
The model defines the columns and the relationships that the truck has.

    Typical Usage example:

    Truck("Mercedes", "Flatbed")
"""
from transport import db


class Truck(db.Model):
    """
    Attributes
        __tablename__: A string that defines the SQLAlchemy table name
        id: A intger that define the primary key of Truck
        brand: A string that defines what brand the Truck is
        type: A string that defines what type the truck is
        eg box, flatbed, freezer, tank etc.
        registration_number: A 8 character string that defines
        registration number of the truck
        missions: A list of missions that the truck is allocated to
    """
    __tablename__ = "Trucks"
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(40), unique=False, nullable=False)
    type = db.Column(db.String(40), unique=False, nullable=False)
    registration_number = db.Column(db.String(8),
                                    unique=False, nullable=False)

    # One to Many relationship with missions
    # back_populates for accessing related
    # transportation worker in mission
    # lazy load for auto loading missions
    missions = db.relationship("Mission", back_populates="truck", lazy=True)
    """ Constructs an object of type Truck"""
    def __init__(self, brand, type, registration_number):
        """ Constructs a transportation worker object"""
        self.brand = brand
        self.type = type
        self.registration_number = registration_number

    def __repr__(self):
        """Returns textual representation of object"""
        return ("{0}, {1}, REG: {2}".format(
            self.brand, self.type, self.registration_number
        ))
