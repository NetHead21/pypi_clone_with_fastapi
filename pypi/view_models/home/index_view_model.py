from typing import List

from pypi.services import package_service, user_service
from pypi.view_models.shared.view_model import ViewModelBase
from starlette.requests import Request


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.release_count: int = 0
        self.user_count: int = 0
        self.package_count: int = 0
        self.packages: List = []

    async def load(self):
        self.release_count: int = await package_service.release_count()
        self.user_count: int = await user_service.user_count()
        self.package_count: int = await package_service.package_count()
        self.packages: List = await package_service.latest_packages(limit=5)
