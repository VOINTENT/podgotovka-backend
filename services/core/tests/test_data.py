from tests.utils.utils import get_random_int, get_random_datetime, get_random_email, get_random_str


class TestAccountTeacherData:
    id = get_random_int()
    edited_at = get_random_datetime()
    email = get_random_email()
    name = get_random_str()
    password = 'qwerty123'
    hash_password = '$2y$12$MkyswyVUDAGfphgolW2i8uxTeenqCfAqQajMM//S7VMAKujXp6GtG'
