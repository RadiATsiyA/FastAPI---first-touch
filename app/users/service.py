from app.users.models import Users

from app.services.base import BaseServices


class UserService(BaseServices):
    model = Users


