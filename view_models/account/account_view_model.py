from starlette.requests import Request
from datetime import datetime
from data.user import User
from view_models.shared.view_model import ViewModelBase


class AccountViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.user = User(
            "Juniven",
            "junivensaavedra@gmail.com",
            "asdr23rsdrw234s",
        )
