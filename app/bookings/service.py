from sqlalchemy import select

from app.database import async_session_maker
from app.bookings.models import Bookings
from app.services.base import BaseServices


class BookingService(BaseServices):
    model = Bookings

