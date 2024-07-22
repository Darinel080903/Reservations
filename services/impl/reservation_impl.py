from abc import ABC

from persistance.models.enum.status import Status
from persistance.repositories.reservation_repository import Reservation_repository
from services.abstract.reservation_abstract import Reservation_service
from web.dto.response.base_response import Base_response
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from datetime import datetime

scheduler = BackgroundScheduler()
scheduler.start()

def convert_time_to_numbers(time_str):
    time_obj = datetime.strptime(time_str, "%H:%M:%S")
    return time_obj.hour, time_obj.minute, time_obj.second


class Reservation_impl(Reservation_service, ABC):
    def __init__(self, reservation_repository: Reservation_repository):
        self.reservation_repository = reservation_repository

    @staticmethod
    def set_reservation_inactive(self, reservation_id):
        reservation = self.reservation_repository.get_by_id(reservation_id)
        reservation.status = Status.INACTIVE
        self.reservation_repository.update_reservation(reservation, reservation_id)

    def get_all(self) -> Base_response:
        try:
            reservations = self.reservation_repository.get_all()
            return Base_response(data=reservations, message="Success", code=200)
        except Exception as e:
            return Base_response(data=None, message=str(e), code=500)

    def add_reservation(self, reservation) -> Base_response:
        try:
            existing_reservations = self.reservation_repository.get_by_user(reservation.user_id)
            for existing_reservation in existing_reservations:
                print(existing_reservation.hour)
                existing_hour = convert_time_to_numbers(existing_reservation.hour)
                new_hour = convert_time_to_numbers(reservation.hour)
                if existing_hour == new_hour:
                    return Base_response(data=None, message="User already has a reservation at this hour", code=400)

            response = requests.get(f'http://75.101.248.20:8000/api/v1/hour/{reservation.establishment_id}')
            if response.status_code != 200:
                return Base_response(data=None, message="Establishment not found", code=404)
            response = response.json()
            hours = response['data']
            open = convert_time_to_numbers(hours['opening_hours'])
            close = convert_time_to_numbers(hours['closing_hours'])
            hour = convert_time_to_numbers(reservation.hour)
            if open < hour < close:
                reservation = self.reservation_repository.add_reservation(reservation)
                run_date = datetime.now() + timedelta(hours=1)
                scheduler.add_job(self.set_reservation_inactive, 'date', run_date=run_date, args=[reservation.id])
                return Base_response(data=reservation, message="Success", code=201)
            return Base_response(data=None, message="Hour not available", code=400)
        except Exception as e:
            return Base_response(data=None, message=str(e), code=500)

    def update_reservation(self, reservation, id: int) -> Base_response:
        try:
            reservation = self.reservation_repository.update_reservation(reservation, id)
            return Base_response(data=reservation, message="Success", code=200)
        except Exception as e:
            return Base_response(data=None, message=str(e), code=500)

    def delete_reservation(self, reservation_id) -> Base_response:
        try:
            self.reservation_repository.delete_reservation(reservation_id)
            return Base_response(data=None, message="Success", code=200)
        except Exception as e:
            return Base_response(data=None, message=str(e), code=500)

    def get_by_uuid(self, uuid) -> Base_response:
        try:
            reservation = self.reservation_repository.get_by_id(uuid)
            return Base_response(data=reservation, message="Success", code=200)
        except Exception as e:
            return Base_response(data=None, message=str(e), code=500)

    def get_by_user(self, user_id) -> Base_response:
        try:
            reservation = self.reservation_repository.get_by_user(user_id)
            return Base_response(data=reservation, message="Success", code=200)
        except Exception as e:
            return Base_response(data=None, message=str(e), code=500)

    def get_by_establishment(self, establishment_id) -> Base_response:
        try:
            reservation = self.reservation_repository.get_by_establishment(establishment_id)
            return Base_response(data=reservation, message="Success", code=200)
        except Exception as e:
            return Base_response(data=None, message=str(e), code=500)

    def get_by_status(self, status) -> Base_response:
        try:
            reservation = self.reservation_repository.get_by_status(status)
            return Base_response(data=reservation, message="Success", code=200)
        except Exception as e:
            return Base_response(data=None, message=str(e), code=500)
