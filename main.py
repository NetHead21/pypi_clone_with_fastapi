from pathlib import Path

import fastapi
import fastapi_chameleon
import uvicorn
from starlette.staticfiles import StaticFiles

from pypi.data import db_session
from pypi.views import home, account, packages

app = fastapi.FastAPI()


def main():
    configure(dev_mode=True)
    uvicorn.run(app, host="127.0.0.1", port=8000)


def configure(dev_mode: bool):
    configure_templates(dev_mode)
    configure_routes()
    configure_db(dev_mode)


def configure_db(dev_mode: bool):
    file = f"{Path(__file__).parent}/pypi/database/pypi.db"
    db_session.global_init(file)


def configure_templates(dev_mode: bool):
    fastapi_chameleon.global_init("pypi/templates", auto_reload=dev_mode)


def configure_routes():
    app.mount("/pypi/static", StaticFiles(directory="pypi/static"), name="static")
    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(packages.router)


if __name__ == "__main__":
    main()
else:
    configure(dev_mode=False)
