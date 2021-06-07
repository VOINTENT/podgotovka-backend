from tests.utils.utils import get_random_int, get_random_datetime, get_random_email, get_random_str


class TestAccountTeacherData:
    id = get_random_int()
    edited_at = get_random_datetime()
    email = get_random_email()
    name = get_random_str()
    password = 'qwerty123'
    hash_password = '$2y$12$MkyswyVUDAGfphgolW2i8uxTeenqCfAqQajMM//S7VMAKujXp6GtG'


class TestStructureData:
    id = 1
    name = 'Начальная школа'


class TestStructureData2:
    id = 2
    name = 'Школа'


class TestStructureData3:
    id = 3
    name = 'Высшая школа'


class TestSubjectData:
    id = get_random_int()
    name = get_random_str()


class TestSubjectData2:
    id = get_random_int()
    name = get_random_str()


class TestCourseData:
    id = get_random_int()
    name = get_random_str()
    structure_id = TestStructureData.id


class TestCourseData2:
    id = get_random_int()
    name = get_random_str()
    structure_id = TestStructureData.id


class TestSubjectCourseData:
    subject_id = TestSubjectData.id
    course_id = TestCourseData.id
