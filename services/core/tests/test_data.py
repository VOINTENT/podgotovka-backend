import datetime

from tests.utils.utils import get_random_int, get_random_datetime, get_random_email, get_random_str, get_random_json


class TestAccountTeacherData:
    id = get_random_int()
    edited_at = get_random_datetime()
    email = get_random_email()
    name = get_random_str()
    last_name = get_random_str()
    middle_name = get_random_str()
    description = get_random_str()
    password = 'qwerty123'
    hash_password = '$2y$12$MkyswyVUDAGfphgolW2i8uxTeenqCfAqQajMM//S7VMAKujXp6GtG'


class TestAccountStudentData:
    id = get_random_int()
    edited_at = get_random_datetime()
    email = get_random_email()
    name = get_random_str()
    last_name = get_random_str()
    middle_name = get_random_str()
    description = get_random_str()
    password = 'qwerty123'
    hash_password = '$2y$12$MkyswyVUDAGfphgolW2i8uxTeenqCfAqQajMM//S7VMAKujXp6GtG'


class TestAccountStudentVkData:
    vk_code = "true1true1true"
    id = get_random_int()
    edited_at = get_random_datetime()
    email = "test@test.com"
    name = 'account'
    last_name = 'student'
    vk_id = 1_000_000


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


class TestSubjectCourseData2:
    id = get_random_int()
    subject_id = TestSubjectData.id
    course_id = TestCourseData.id
    name = f"{TestSubjectData.name} ({TestCourseData.name})"


class TestSubjectCourseData3:
    id = get_random_int()
    subject_id = TestSubjectData2.id
    course_id = TestCourseData.id
    name = f"{TestSubjectData2.name} ({TestCourseData.name})"


class TestHomeworkTestData:
    id = get_random_int()


class TestQuestionData:
    id = get_random_int()
    homework_test_id = TestHomeworkTestData.id
    name = get_random_str()
    description = get_random_json()
    answer_type = 'one'
    count_attempts = get_random_int(10)


class TestQuestionData2:
    id = get_random_int()
    homework_test_id = TestHomeworkTestData.id
    name = get_random_str()
    description = get_random_json()
    answer_type = 'many'
    count_attempts = get_random_int(10)


class TestHomeworkData:
    id = get_random_int()
    homework_type = 'test'
    homework_without_answer_id = None
    homework_test_id = TestHomeworkTestData.id


class TestLessonData:
    id = get_random_int()
    name = get_random_str()
    description = get_random_str()
    youtube_link = get_random_str()
    time_start = datetime.datetime(year=2021, month=1, day=1, hour=10, minute=0)
    time_finish = datetime.time(hour=11, minute=0)
    text = get_random_json()
    is_published = True
    subject = TestSubjectData
    course = TestCourseData
    homework_id = TestHomeworkData.id
    account_teacher_id = TestAccountTeacherData.id
    is_watched = False


class TestLessonData2:
    id = get_random_int()
    name = get_random_str()
    description = get_random_str()
    youtube_link = get_random_str()
    time_start = datetime.datetime(year=2021, month=2, day=1, hour=10, minute=0)
    time_finish = datetime.time(hour=13, minute=0)
    text = get_random_json()
    is_published = True
    subject = TestSubjectData2
    course = TestCourseData2
    homework_id = None
    account_teacher_id = TestAccountTeacherData.id
    is_watched = False


class TestLessonFileData:
    id = get_random_int()
    name = get_random_str()
    file_link = get_random_str()
    lesson_id = TestLessonData.id


class TestLessonFileData2:
    id = get_random_int()
    name = get_random_str()
    file_link = get_random_str()
    lesson_id = TestLessonData.id


class TestAnswerVariantData:
    id = get_random_int()
    test_question_id = TestQuestionData.id
    name = get_random_str()
    is_right = True


class TestAnswerVariantData2:
    id = get_random_int()
    test_question_id = TestQuestionData.id
    name = get_random_str()
    is_right = False


class TestAnswerVariantData3:
    id = get_random_int()
    test_question_id = TestQuestionData2.id
    name = get_random_str()
    is_right = True


class TestAnswerVariantData4:
    id = get_random_int()
    test_question_id = TestQuestionData2.id
    name = get_random_str()
    is_right = False
