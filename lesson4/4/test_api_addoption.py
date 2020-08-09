import requests


def test_check_url(url, code):
    response = requests.get(url)
    assert response.status_code == int(code)



