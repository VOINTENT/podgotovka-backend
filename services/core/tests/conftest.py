from typing import Generator

import pytest
from starlette.testclient import TestClient

from src.internal.drivers.fast_api import FastAPIServer
from tests.utils.db import truncate_tables


@pytest.fixture(scope='session')
def client() -> Generator:
    app = FastAPIServer.get_test_app()
    with TestClient(app) as client:
        yield client


@pytest.fixture()
def truncate():
    truncate_tables()
    yield
