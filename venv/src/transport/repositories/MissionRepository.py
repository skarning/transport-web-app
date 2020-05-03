from transport.models.Mission import Mission
from transport import db


class MissionRepository:

    def add(self, mission):
        db.session.add(mission)
        db.session.commit()

    def delete(self, mission):
        db.session.delete()
        db.session.commit()

    def get_all(self):
        return Mission.query.order_by(Mission.date).all()
