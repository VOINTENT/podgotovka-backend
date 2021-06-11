from typing import Generator

import pytest
from starlette.testclient import TestClient

from src.internal.drivers.fast_api import FastAPIServer
from tests.test_data import TestAccountTeacherData, TestSubjectData, TestSubjectData2, TestCourseData, TestCourseData2, \
    TestSubjectCourseData, TestStructureData, TestStructureData2, TestStructureData3, TestLessonData, TestLessonData2, \
    TestHomeworkData, TestHomeworkTestData, TestQuestionData, TestQuestionData2, TestLessonFileData, \
    TestLessonFileData2, TestAnswerVariantData, TestAnswerVariantData2, TestAnswerVariantData3, TestAnswerVariantData4, \
    TestAccountStudentData, TestAccountStudentVkData
from tests.utils.db import truncate_tables, create_account_teacher, create_subject, create_course, \
    create_subject_course, create_structure, create_lesson, create_homework, create_homework_test, create_test_question, \
    create_lesson_file, create_answer_variant, create_account_student, create_account_student_vk


@pytest.fixture(scope='session')
def client() -> Generator:
    app = FastAPIServer.get_test_app()
    with TestClient(app) as client:
        yield client


@pytest.fixture()
def truncate():
    truncate_tables()
    yield


@pytest.fixture()
def teacher_account():
    create_account_teacher(
        id=TestAccountTeacherData.id,
        edited_at=TestAccountTeacherData.edited_at,
        email=TestAccountTeacherData.email,
        name=TestAccountTeacherData.name,
        hash_password=TestAccountTeacherData.hash_password
    )


@pytest.fixture()
def account_student():
    create_account_student(
        id=TestAccountStudentData.id,
        edited_at=TestAccountStudentData.edited_at,
        email=TestAccountStudentData.email,
        name=TestAccountStudentData.name,
        hash_password=TestAccountStudentData.hash_password
    )


@pytest.fixture()
def account_student_vk():
    create_account_student_vk(
        id=TestAccountStudentVkData.id,
        edited_at=TestAccountStudentVkData.edited_at,
        email=TestAccountStudentVkData.email,
        name=TestAccountStudentVkData.name,
        last_name=TestAccountStudentVkData.last_name,
        vk_id=TestAccountStudentVkData.vk_id
    )


@pytest.fixture()
def teacher_account_access_token(teacher_account, client: TestClient):
    response = client.post('/core/v1/accounts-teacher/auth/base', data={
        'username': TestAccountTeacherData.email,
        'password': TestAccountTeacherData.password
    })
    return response.json()['access_token']


@pytest.fixture()
def subjects():
    create_subject(id=TestSubjectData.id, name=TestSubjectData.name)
    create_subject(id=TestSubjectData2.id, name=TestSubjectData2.name)


@pytest.fixture()
def courses():
    create_course(id=TestCourseData.id, name=TestCourseData.name, structure_id=TestCourseData.structure_id)
    create_course(id=TestCourseData2.id, name=TestCourseData2.name, structure_id=TestCourseData2.structure_id)


@pytest.fixture()
def subject_course():
    create_subject_course(subject_id=TestSubjectCourseData.subject_id, course_id=TestSubjectCourseData.course_id)


@pytest.fixture()
def structures():
    create_structure(id=TestStructureData.id, name=TestStructureData.name)
    create_structure(id=TestStructureData2.id, name=TestStructureData2.name)
    create_structure(id=TestStructureData3.id, name=TestStructureData3.name)


@pytest.fixture()
def lesson():
    create_lesson(id=TestLessonData.id, name=TestLessonData.name, description=TestLessonData.description,
                  youtube_link=TestLessonData.youtube_link, time_start=TestLessonData.time_start,
                  time_finish=TestLessonData.time_finish, text=TestLessonData.text,
                  is_published=TestLessonData.is_published, subject_id=TestLessonData.subject.id,
                  course_id=TestLessonData.course.id, homework_id=TestLessonData.homework_id,
                  account_teacher_id=TestLessonData.account_teacher_id)

    create_lesson_file(id=TestLessonFileData.id, name=TestLessonFileData.name, file_link=TestLessonFileData.file_link,
                       lesson_id=TestLessonFileData.lesson_id)

    create_lesson_file(id=TestLessonFileData2.id, name=TestLessonFileData2.name,
                       file_link=TestLessonFileData2.file_link,
                       lesson_id=TestLessonFileData2.lesson_id)


@pytest.fixture()
def lesson2():
    create_lesson(id=TestLessonData2.id, name=TestLessonData2.name, description=TestLessonData2.description,
                  youtube_link=TestLessonData2.youtube_link, time_start=TestLessonData2.time_start,
                  time_finish=TestLessonData2.time_finish, text=TestLessonData2.text,
                  is_published=TestLessonData2.is_published, subject_id=TestLessonData2.subject.id,
                  course_id=TestLessonData2.course.id, homework_id=TestLessonData2.homework_id,
                  account_teacher_id=TestLessonData2.account_teacher_id)


@pytest.fixture()
def homework():
    create_homework_test(id=TestHomeworkTestData.id)

    create_test_question(id=TestQuestionData.id, homework_test_id=TestQuestionData.homework_test_id,
                         name=TestQuestionData.name, description=TestQuestionData.description,
                         answer_type=TestQuestionData.answer_type, count_attempts=TestQuestionData.count_attempts)

    create_test_question(id=TestQuestionData2.id, homework_test_id=TestQuestionData2.homework_test_id,
                         name=TestQuestionData2.name, description=TestQuestionData2.description,
                         answer_type=TestQuestionData2.answer_type, count_attempts=TestQuestionData2.count_attempts)

    create_answer_variant(id=TestAnswerVariantData.id, name=TestAnswerVariantData.name,
                          is_right=TestAnswerVariantData.is_right,
                          test_question_id=TestAnswerVariantData.test_question_id)
    create_answer_variant(id=TestAnswerVariantData2.id, name=TestAnswerVariantData2.name,
                          is_right=TestAnswerVariantData2.is_right,
                          test_question_id=TestAnswerVariantData2.test_question_id)
    create_answer_variant(id=TestAnswerVariantData3.id, name=TestAnswerVariantData3.name,
                          is_right=TestAnswerVariantData3.is_right,
                          test_question_id=TestAnswerVariantData3.test_question_id)
    create_answer_variant(id=TestAnswerVariantData4.id, name=TestAnswerVariantData4.name,
                          is_right=TestAnswerVariantData4.is_right,
                          test_question_id=TestAnswerVariantData4.test_question_id)

    create_homework(id=TestHomeworkData.id, homework_type=TestHomeworkData.homework_type,
                    homework_without_answer_id=TestHomeworkData.homework_without_answer_id,
                    homework_test_id=TestHomeworkData.homework_test_id)
