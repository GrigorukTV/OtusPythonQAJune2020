import pytest
import json

# проверка статуса запроса страницы с картинкой
def test_one(api_client):
    res = api_client.get(
        path="/api/breed/hound/afghan/images"
    )
    assert res.status_code==200

# проверка существования значения
def test_three(api_client):
    res = api_client.get(
        path="/api/breed/hound/list"
    )
    item = 'blood'
    assert (item in res.json()['message']) == True

# проверка отсутствия значения
def test_four(api_client):
    res = api_client.post(
        path="/api/breed/hound/images",
        params={'userId':0}
    )
    assert res.status_code==405

# проверка количества возвращаемых картинок
@pytest.mark.parametrize('count', [1,2,3])
def test_two(api_client, count):
    res = api_client.get(
        path="/api/breed/hound/afghan/images/random/"+str(count),
    )
    assert res.status_code==200
    assert len(res.json()['message']) == count

# проверка статуса запроса страницы с картинкой по определенной породе
@pytest.mark.parametrize('breed', ["afghan", "basset", "blood"])
def test_five(api_client, breed):
    res = api_client.get(
        path="/api/breed/hound/" + breed + "/images"
    )
    assert res.status_code==200