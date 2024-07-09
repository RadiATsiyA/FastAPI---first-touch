from sqlalchemy.orm import relationship

from app.database import Base
from sqlalchemy import Column, Integer, String, JSON, ForeignKey


class Hotels(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    services = Column(JSON, nullable=False)
    rooms_quantity = Column(Integer, nullable=False)
    image_id = Column(Integer, nullable=False)
    rooms = relationship("Rooms", backref="hotel", cascade="all, delete")


class Rooms(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True)
    hotel_id = Column(ForeignKey("hotels.id", ondelete="CASCADE"), nullable=False)
    name = Column(String)
    description = Column(String, nullable=True)
    price = Column(Integer, nullable=False)
    services = Column(JSON, nullable=True)
    quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)
