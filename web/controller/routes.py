from fastapi import APIRouter

from persistance.models.enum.status import Status
from persistance.models.reservation_entity import Reservation_entity
from services.impl.reservation_impl import Reservation_impl
from persistance.repositories.reservation_repository import Reservation_repository
from web.dto.request.reservation_request import Reservation_request

controller = APIRouter()
repository = Reservation_repository()
service = Reservation_impl(repository)

base_url = "/api/v1"


@controller.post(base_url + "/create/")
def create_reservation(reservation: Reservation_request):
    return service.add_reservation(reservation)


@controller.put(base_url + "/update/{reservation_id}")
def update_reservation(reservation: Reservation_request, reservation_id: int):
    return service.update_reservation(reservation, reservation_id)


@controller.get(base_url + "/")
def get_reservations():
    return service.get_all()


@controller.get(base_url + "/{reservation_id}")
def get_reservation(reservation_id: int):
    return service.get_by_uuid(reservation_id)


@controller.get(base_url + "/user/{user_id}")
def get_reservations_by_user(user_id: str):
    return service.get_by_user(user_id)


@controller.get(base_url + "/establishment/{establishment_id}")
def get_reservations_by_establishment(establishment_id: str):
    return service.get_by_establishment(establishment_id)


@controller.get(base_url + "/status/{status}")
def get_reservations_by_status(status: Status):
    return service.get_by_status(status)
