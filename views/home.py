import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()


@router.get("/")
@template()
def index(user: str = "NetHead21"):
    return {"user_name": user}


@router.get("/about")
@template()
def about():
    return {}
