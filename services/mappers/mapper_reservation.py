from persistance.models.reservation_entity import Reservation_entity
from persistance.schema.model_factory import Reservation
from web.dto.request.reservation_request import Reservation_request


class Mapper_reservation:
    @staticmethod
    def db_to_model(reservation: Reservation) -> Reservation_entity:
        return Reservation_entity(
            id=reservation.id,
            user_id=reservation.user_id,
            establishment_id=reservation.establishment_id,
            service=reservation.service,
            date=reservation.date,
            hour=reservation.hour,
            status=reservation.status
        )

    @staticmethod
    def model_to_db(reservation: Reservation_entity) -> Reservation:
        return Reservation(
            user_id=reservation.user_id,
            establishment_id=reservation.establishment_id,
            service=reservation.service,
            date=reservation.date,
            hour=reservation.hour,
            status=reservation.status
        )

    @staticmethod
    def request_to_db(reservation: Reservation_request) -> Reservation:
        return Reservation(
            user_id=reservation.user_id,
            establishment_id=reservation.establishment_id,
            service=reservation.service,
            date=reservation.date,
            hour=reservation.hour,
            status=reservation.status
        )

    @staticmethod
    def request_to_model(reservation: Reservation_request) -> Reservation_entity:
        return Reservation_entity(
            id=None,
            user_id=reservation.user_id,
            establishment_id=reservation.establishment_id,
            service=reservation.service,
            date=reservation.date,
            hour=reservation.hour,
            status=reservation.status
        )