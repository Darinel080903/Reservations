from pydantic import BaseModel

from persistance.models.enum.status import Status


class Reservation_entity(BaseModel):
    id: str
    user_id: str
    establishment_id: str
    service: str
    date: str
    hour: str
    status: Status
