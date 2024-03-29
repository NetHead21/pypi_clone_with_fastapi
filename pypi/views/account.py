import asyncio

import fastapi
from starlette import status

from starlette.requests import Request
from fastapi_chameleon import template

from pypi.infrastructure import cookie_auth
from pypi.services import user_service
from pypi.view_models.account.account_view_model import AccountViewModel
from pypi.view_models.account.login_view_model import LoginViewModel
from pypi.view_models.account.register_view_model import RegisterViewModel


router = fastapi.APIRouter()


@router.get("/account")
@template()
async def index(request: Request):
    vm = AccountViewModel(request)
    await vm.load()
    return vm.to_dict()


@router.get("/account/register")
@template()
async def register(request: Request):
    vm = RegisterViewModel(request)
    await vm.load()
    return vm.to_dict()


@router.post("/account/register")
@template()
async def register(request: Request):
    vm = RegisterViewModel(request)
    await vm.load()

    if vm.error:
        return vm.to_dict()

    # Create the account
    account = await user_service.create_account(vm.name, vm.email, vm.password)

    # Login user
    response = fastapi.responses.RedirectResponse(
        url="/account", status_code=status.HTTP_302_FOUND
    )
    cookie_auth.set_auth(response, account.id)

    return response


@router.get("/account/login")
@template()
def login(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()


@router.post("/account/login")
@template(template_file="account/login.pt")
async def login_post(request: Request):
    vm = LoginViewModel(request)
    await vm.load()

    if vm.error:
        return vm.to_dict()

    user = await user_service.login_user(vm.email, vm.password)
    if not user:
        await asyncio.sleep(5)
        vm.error = "The account does not exist or the password is wrong."
        return vm.to_dict()

    resp = fastapi.responses.RedirectResponse(
        "/account", status_code=status.HTTP_302_FOUND
    )
    cookie_auth.set_auth(resp, user.id)

    return resp


@router.get("/account/logout")
def logout():
    response = fastapi.responses.RedirectResponse(
        url="/", status_code=status.HTTP_302_FOUND
    )
    cookie_auth.logout(response)

    return response
