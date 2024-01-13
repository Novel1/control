import pydantic
import fastapi

from app.api.router import router
from app.exceptions import handlers as exc_handlers, http as http_exceptions
from tortoise.contrib.fastapi import register_tortoise

from app.db.conf import TORTOISE_ORM


def setup():
    app = fastapi.FastAPI()
    app.include_router(router)

    register_tortoise(
        app=app,
        config=TORTOISE_ORM,
        generate_schemas=True,
        add_exception_handlers=True,
    )

    app.exception_handler(pydantic.ValidationError)(exc_handlers.query_params_exc_handler)
    app.exception_handler(http_exceptions.BaseHTTPException)(exc_handlers.request_exc_handler)
    app.exception_handler(500)(exc_handlers.internal_exc_handler)

    return app


if __name__ == "__main__":
    import uvicorn

    app = setup()

    uvicorn.run(app, host='0.0.0.0', port=7000)
