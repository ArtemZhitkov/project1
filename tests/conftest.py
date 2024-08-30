import pytest


@pytest.fixture
def numbers():
    return 2, 3


@pytest.fixture
def numbers():
    return -2, 3


@pytest.fixture
def numbers():
    return 0, 0


@pytest.fixture
def numbers_2():
    return -2, 3


@pytest.fixture
def numbers():
    return 0, 0
