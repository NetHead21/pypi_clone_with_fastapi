from typing import Optional

from pypi.data.release import Release
from pypi.data.package import Package
from pypi.services import package_service
from pypi.view_models.shared.view_model import ViewModelBase
from starlette.requests import Request


class DetailsViewModel(ViewModelBase):
    def __init__(self, package_name: str, request: Request):
        super().__init__(request)

        self.package_name = package_name
        self.latest_version = "0.0.0"
        self.is_latest = True
        self.maintainers = []
        self.package: Optional[Package] = None
        self.latest_release: Optional[Release] = None

    async def load(self):
        self.package = await package_service.get_package_by_id(self.package_name)
        self.latest_release = await package_service.get_latest_release_for_package(
            self.package_name
        )

        if not self.package or not self.latest_release:
            return

        latest_version = self.latest_release
        self.latest_version = f"{latest_version.major_ver}.{latest_version.minor_ver}.{latest_version.build_ver}"
        self.maintainers = []
