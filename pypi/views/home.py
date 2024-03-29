import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from pypi.view_models.home.index_view_model import IndexViewModel
from pypi.view_models.shared.view_model import ViewModelBase

router = fastapi.APIRouter()


@router.get("/")
@template()
async def index(request: Request):
    vm = IndexViewModel(request)
    await vm.load()
    return vm.to_dict()


@router.get("/about")
@template()
def about(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()
