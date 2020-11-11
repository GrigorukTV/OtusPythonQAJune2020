import pytest


def pytest_addoption(parser):
    parser.addoption("--browser",
                        action="store",
                        help="browser",
                        choices=['chrome','firefox'])
    parser.addoption("--url",
                        default="http://localhost/",
                        help="This is request url")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def url(request):
    return request.config.getoption("--url")


