from typing import Optional

from starlette.requests import Request
from pypi.data.user import User
from pypi.view_models.shared.view_model import ViewModelBase
from pypi.services import user_service


class AccountViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.user: Optional[User] = None

    async def load(self):
        self.user = await user_service.get_user_by_id(self.user_id)
