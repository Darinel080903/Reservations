from abc import ABC, abstractmethod

from persistance.repositories.reservation_repository import Reservation_repository
from web.dto.response.base_response import Base_response


class Reservation_service(ABC):
    @abstractmethod
    def __init__(self, reservation_repository: Reservation_repository):
        self.reservation_repository = reservation_repository

    @abstractmethod
    def get_all(self) -> Base_response:
        raise NotImplemented

    @abstractmethod
    def add_reservation(self, reservation) -> Base_response:
        raise NotImplemented

    @abstractmethod
    def update_reservation(self, reservation, id: int) -> Base_response:
        raise NotImplemented

    @abstractmethod
    def delete_reservation(self, reservation_id) -> Base_response:
        raise NotImplemented

    @abstractmethod
    def get_by_uuid(self, uuid) -> Base_response:
        raise NotImplemented

    @abstractmethod
    def get_by_user(self, user_id) -> Base_response:
        raise NotImplemented

    @abstractmethod
    def get_by_establishment(self, establishment_id) -> Base_response:
        raise NotImplemented

    @abstractmethod
    def get_by_status(self, status) -> Base_response:
        raise NotImplemented
