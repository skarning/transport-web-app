from transport.models.Truck import Truck
from transport import db


class TruckRepository:

    def add(transportation_worker):
        db.session.add(transportation_worker)
        db.session.commit()

    def delete(transportation_worker):
        db.session.delete(transportation_worker)
        db.session.commit()

    def get_all():
        Truck.query.all()
