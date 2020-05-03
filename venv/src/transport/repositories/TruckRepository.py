from transport.models.Truck import Truck
from transport import db


class TruckRepository:

    def add(self, transportation_worker):
        db.session.add(transportation_worker)
        db.session.commit()

    def delete(self, transportation_worker):
        db.session.delete(transportation_worker)
        db.session.commit()

    def get_all(self):
        return Truck.query.all()
