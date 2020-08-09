import pytest
import requests


class testAPI:

    def __init__(self, base_address):
        self.base_address = base_address

    def post(self, path="/", params=None, data=None, headers=None):
        url = self.base_address + path
        print("POST request to {}".format(url))
        return requests.post(url=url, params=params, data=data, headers=headers)

    def get(self, path="/", params=None):
        url = self.base_address + path
        print("GET request to {}".format(url))
        return requests.get(url=url, params=params)

    def put(self, path="/", params=None, data=None, headers=None):
        url = self.base_address + path
        print("PUT request to {}".format(url))
        return requests.put(url=url, params=params, data=data)

    def delete(self, path="/", params=None):
        url = self.base_address + path
        print("DELETE request to {}".format(url))
        return requests.delete(url=url, params=params)

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://jsonplaceholder.typicode.com",
        help="This is request url"
    )


@pytest.fixture(scope="session")
def api_client(request):
    base_url = request.config.getoption("--url")
    return testAPI(base_address=base_url)