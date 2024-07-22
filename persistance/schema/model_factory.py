from sqlalchemy import Column, String, Enum, Integer
from configuration.db import Base, engine
from persistance.models.enum.status import Status


class Reservation(Base):
    __tablename__ = 'reservation'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(255), nullable=False)
    establishment_id = Column(String(255), nullable=False)
    service = Column(String(255), nullable=False)
    date = Column(String(255), nullable=False)
    hour = Column(String(255), nullable=False)
    detail = Column(String(255), nullable=True)
    status = Column(Enum(Status), nullable=False)


Base.metadata.create_all(engine)
