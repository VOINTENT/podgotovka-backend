from starlette.testclient import TestClient

from tests.test_data import TestAccountTeacherData


def test_auth_base(client: TestClient, truncate, teacher_account):
    response = client.post('/core/v1/accounts-teacher/auth/base', data={
      'username': TestAccountTeacherData.email,
      'password': TestAccountTeacherData.password
    })

    assert response.status_code == 200
    result = response.json()
    assert isinstance(result['access_token'], str)
    assert result['token_type'] == 'bearer'
