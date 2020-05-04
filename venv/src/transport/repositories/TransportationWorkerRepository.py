from transport.models.TransportationWorker import TransportationWorker
from transport import db


class TransportationWorkerRepository:

    def add(self, transportation_worker):
        db.session.add(transportation_worker)
        db.session.commit()

    def delete(self, transportation_worker):
        db.session.delete(transportation_worker)
        db.session.commit()

    def get_all(self):
        return TransportationWorker.query.order_by(
            TransportationWorker.full_name
        ).all()

    def get_by_id(self, id):
        return TransportationWorker.query.get(id)
