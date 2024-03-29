import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from pypi.view_models.packages.details_view_model import DetailsViewModel

router = fastapi.APIRouter()


@router.get("/project/{package_name}")
@template(template_file="packages/details.pt")
async def details(package_name: str, request: Request):
    vm = DetailsViewModel(package_name, request)
    await vm.load()
    return vm.to_dict()
