from typing import List

from services import package_service, user_service
from view_models.shared.view_model import ViewModelBase
from starlette.requests import Request


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.release_count: int = package_service.release_count()
        self.user_count: int = user_service.user_count()
        self.package_count: int = package_service.package_count()
        self.packages: List = package_service.latest_packages(limit=5)