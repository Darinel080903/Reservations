from configuration.db import SessionLocal
from persistance.schema.model_factory import Reservation
from services.mappers.mapper_reservation import Mapper_reservation


class Reservation_repository:
    def __init__(self):
        self.db = SessionLocal()

    def add_reservation(self, reservation):
        model = Mapper_reservation.request_to_db(reservation)
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        self.db.close()
        return reservation

    def get_all(self):
        reservations = self.db.query(Reservation).all()
        self.db.close()
        return reservations

    def get_by_id(self, reservation_id):
        return self.db.query(Reservation).filter(Reservation.id == reservation_id).first()

    def get_by_establishment(self, uuid: str):
        return self.db.query(Reservation).filter(Reservation.establishment_id == uuid).all()

    def get_by_user(self, uuid: str):
        return self.db.query(Reservation).filter(Reservation.user_id == uuid).all()

    def update_reservation(self, reservation, reservation_id):
        reservation_db = self.db.query(Reservation).filter(Reservation.id == reservation_id).first()
        reservation_db.status = reservation.status
        self.db.commit()
        self.db.refresh(reservation_db)
        self.db.close()
        return reservation_db

    def delete_reservation(self, reservation_id):
        reservation_db = self.db.query(Reservation).filter(Reservation.id == reservation_id).first()
        self.db.delete(reservation_db)
        self.db.commit()
        self.db.close()

    def get_by_status(self, status):
        return self.db.query(Reservation).filter(Reservation.status == status).all()
