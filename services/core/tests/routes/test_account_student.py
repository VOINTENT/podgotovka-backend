from starlette.testclient import TestClient

from tests.test_data import TestAccountStudentData, TestAccountStudentVkData
from tests.utils.db import run_query
from tests.utils.utils import get_auth_headers


def test_account_student_auth_base(client: TestClient, truncate, account_student):
    response = client.post('/core/v1/accounts-student/auth/base', data={
        'username': TestAccountStudentData.email,
        'password': TestAccountStudentData.password
    })

    assert response.status_code == 200
    result = response.json()
    assert isinstance(result['access_token'], str)
    assert result['token_type'] == 'bearer'


def test_account_student_reg_base(client: TestClient, truncate):
    response = client.post('/core/v1/accounts-student/register', json={
        "email": TestAccountStudentData.email,
        "name": TestAccountStudentData.name,
        "password": TestAccountStudentData.password
    })
    assert response.status_code == 200
    result = response.json()
    assert isinstance(result['access_token'], str)
    assert result['token_type'] == 'bearer'

    student_info = run_query("SELECT email, name, hash_password FROM account_student WHERE email=$1",
                             TestAccountStudentData.email)[0]

    assert student_info[0] == TestAccountStudentData.email
    assert student_info[1] == TestAccountStudentData.name


def test_account_student_auth_vk(client: TestClient, truncate, account_student_vk):
    response = client.post('/core/v1/accounts-student/auth/vk', json={
        "code": TestAccountStudentVkData.vk_code
    })
    assert response.status_code == 200
    result = response.json()

    assert isinstance(result['access_token'], str)
    assert result['token_type'] == 'bearer'


def test_account_student_auth_vk_invalid_code(client: TestClient, truncate, account_student_vk):
    response = client.post('/core/v1/accounts-student/auth/vk', json={
        "code": "qwerty12310"
    })
    assert response.status_code == 401


def test_account_student_reg_vk(client: TestClient, truncate):
    response = client.post('/core/v1/accounts-student/auth/vk', json={
        "code": TestAccountStudentVkData.vk_code
    })
    assert response.status_code == 200
    result = response.json()

    assert isinstance(result['access_token'], str)
    assert result['token_type'] == 'bearer'

    student_info = run_query("SELECT email, name,last_name,vk_id FROM account_student WHERE vk_id=$1",
                             TestAccountStudentVkData.vk_id)[0]

    assert student_info[0] == TestAccountStudentVkData.email
    assert student_info[1] == TestAccountStudentVkData.name
    assert student_info[2] == TestAccountStudentVkData.last_name
    assert student_info[3] == TestAccountStudentVkData.vk_id


def test_get_detail_info(client: TestClient, truncate, account_student, access_token_student):
    response = client.get('/core/v1/accounts-student/me', headers=get_auth_headers(access_token_student))

    assert response.status_code == 200

    result = response.json()

    assert result['id'] == TestAccountStudentData.id
    assert result['name'] == TestAccountStudentData.name
    assert result['last_name'] == TestAccountStudentData.last_name
    assert result['middle_name'] == TestAccountStudentData.middle_name
    assert result['email'] == TestAccountStudentData.email
    assert result['description'] == TestAccountStudentData.description
    assert result['photo_link'] is None
    assert result['vk_id'] is None
