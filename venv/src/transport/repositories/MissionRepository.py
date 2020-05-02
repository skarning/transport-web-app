from transport.models.Mission import Mission
from transport import db


class MissionRepository:

    def add(mission):
        db.session.add(mission)
        db.session.commit()

    def delete(mission):
        db.session.delete()
        db.session.commit()

    def get_all():
        return Mission.query.order_by(Mission.date).all()
