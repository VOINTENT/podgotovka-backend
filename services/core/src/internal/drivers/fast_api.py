import logging

from fastapi import FastAPI

from src.configs.db import DB_HOST, DB_USER, DB_PASSWORD, DB_PORT, PRIMARY_DB_NAME, LOGS_DB_NAME
from src.configs.server import DEBUG, TITLE_API, DESCRIPTION_API, VERSION_API
from src.internal.drivers.async_pg import AsyncPg
from src.internal.servers.http.api.general import general_router
from src.internal.servers.http.middlewares.logs import add_logs


class FastAPIServer:

    @staticmethod
    def get_app() -> FastAPI:
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        app = FastAPI(
            debug=DEBUG,
            title=TITLE_API,
            description=DESCRIPTION_API,
            version=VERSION_API,
            docs_url='/core/v1/docs',
            openapi_url='/core/v1/openapi.json'
        )

        app.include_router(general_router)
        add_logs(app)

        @app.on_event('startup')
        async def init_primary_db():
            await AsyncPg.init_primary_db(DB_HOST, DB_USER, DB_PASSWORD, DB_PORT, PRIMARY_DB_NAME)
            await AsyncPg.init_log_db(DB_HOST, DB_USER, DB_PASSWORD, DB_PORT, LOGS_DB_NAME)

        @app.on_event('shutdown')
        async def close_primary_db():
            await AsyncPg.close_primary_pool_db()
            await AsyncPg.close_logs_pool_db()

        return app

    @staticmethod
    def get_test_app() -> FastAPI:
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        app = FastAPI(
            debug=DEBUG,
            title=TITLE_API,
            description=DESCRIPTION_API,
            version=VERSION_API,
            docs_url='/core/v1/docs',
            openapi_url='/core/v1/openapi.json'
        )

        app.include_router(general_router)

        @app.on_event('startup')
        async def init_primary_db():
            await AsyncPg.init_primary_db(DB_HOST, DB_USER, DB_PASSWORD, DB_PORT, PRIMARY_DB_NAME,
                                          min_size=10, max_size=10)

        @app.on_event('shutdown')
        async def close_primary_db():
            await AsyncPg.close_primary_pool_db()

        return app
