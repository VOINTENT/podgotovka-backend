from starlette.testclient import TestClient

from tests.test_data import TestAccountTeacherData
from tests.utils.utils import get_auth_headers


def test_auth_base(client: TestClient, truncate, account_teacher):
    response = client.post('/core/v1/accounts-teacher/auth/base', data={
        'username': TestAccountTeacherData.email,
        'password': TestAccountTeacherData.password
    })

    assert response.status_code == 200
    result = response.json()
    assert isinstance(result['access_token'], str)
    assert result['token_type'] == 'bearer'


def test_get_detail_info(client: TestClient, truncate, account_teacher, access_token_teacher):
    response = client.get('/core/v1/accounts-teacher/me', headers=get_auth_headers(access_token_teacher))

    assert response.status_code == 200

    result = response.json()

    assert result['id'] == TestAccountTeacherData.id
    assert result['name'] == TestAccountTeacherData.name
    assert result['last_name'] == TestAccountTeacherData.last_name
    assert result['middle_name'] == TestAccountTeacherData.middle_name
    assert result['email'] == TestAccountTeacherData.email
    assert result['description'] == TestAccountTeacherData.description
    assert result['photo_link'] is None
