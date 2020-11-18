import pytest

# проверка на существование добавленных данных
def test_api_post_one(api_client):
    res = api_client.post(
        path = "/comments",
        data = {'postId': 77, 'name': 'vero', 'email': 'tests@mail.ru', 'body': 'harum'}
    )
    assert res.json()['name'] == 'vero'

# проверка на обновление данных
def test_api_put_two(api_client):
    res = api_client.put(
        path = "/comments/67",
        data = {'email': 'tests@mail.ru'}
    )
    assert res.json()['email'] == 'tests@mail.ru'

# проверка на удаление данных
def test_api_delete_three(api_client):
    res = api_client.delete(
        path = "/comments/67"
    )
    assert (res.json()) == {}

# проверка на обновление данных
@pytest.mark.parametrize('id, userId, completed', [(5, 10, 'true'), (6, 22, 'false')])
def test_api_put_four(api_client, id, userId, completed):
    res = api_client.put(
        path = "/todos/"+str(id),
        data = {'userId': userId, 'completed': completed}
    )
    assert (res.json()['completed']) == completed

# проверка на существование id
@pytest.mark.parametrize('id',  [5, 69, 7, 88])
def test_api_put_four(api_client, id,  ):
    res = api_client.get(
        path = "/todos/"+str(id),
    )
    assert (res.json()['id']) == id