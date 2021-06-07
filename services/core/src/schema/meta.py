from datetime import datetime

import sqlalchemy
from sqlalchemy import Table, Column, Integer, Sequence, DateTime, func, Text, CheckConstraint, ForeignKey, \
    UniqueConstraint, Date, Time, Boolean, SmallInteger
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import expression

naming_convention = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),
    'ix': 'ix__%(table_name)s__%(all_column_names)s',
    'uq': 'uq__%(table_name)s__%(all_column_names)s',
    'ck': 'ck__%(table_name)s__%(all_column_names)s',
    'fk': (
        'fk__%(table_name)s__%(all_column_names)s__'
        '%(referred_table_name)s'
    ),
    'pk': 'pk__%(table_name)s'
}

metadata = sqlalchemy.MetaData(naming_convention=naming_convention)

account_teacher_table = Table(
    'account_teacher',
    metadata,
    Column('id', Integer, default=Sequence('account_teacher_seq'), primary_key=True),
    Column('created_at', DateTime, nullable=False, server_default=func.current_timestamp()),
    Column('edited_at', DateTime, nullable=False, server_default=func.current_timestamp(), onupdate=datetime.now),
    Column('email', Text, CheckConstraint('char_length(email) >= 4 AND char_length(email) <= 100'), nullable=False,
           unique=True),
    Column('name', Text, CheckConstraint('char_length(name) >= 1 AND char_length(email) <= 100'), nullable=False),
    Column('last_name', Text, CheckConstraint('char_length(last_name) >= 1 AND char_length(last_name) <= 100')),
    Column('middle_name', Text, CheckConstraint('char_length(middle_name) >= 1 AND char_length(middle_name) <= 100')),
    Column('photo_link', Text, CheckConstraint('char_length(photo_link) >= 1 AND char_length(photo_link) <= 1000')),
    Column('description', Text, CheckConstraint('char_length(description) >= 1 AND char_length(description) <= 5000')),
    Column('hash_password', Text,
           CheckConstraint('char_length(hash_password) >= 1 AND char_length(hash_password) <= 500'), nullable=False)
)

structure_table = Table(
    'structure',
    metadata,
    Column('id', Integer, default=Sequence('structure_seq'), primary_key=True),
    Column('name', Text, CheckConstraint("name IN ('primary-school', 'school', 'high-school')"), nullable=False, unique=True),
)

course_table = Table(
    'course',
    metadata,
    Column('id', Integer, default=Sequence('course_seq'), primary_key=True),
    Column('created_at', DateTime, nullable=False, server_default=func.current_timestamp()),
    Column('edited_at', DateTime, nullable=False, server_default=func.current_timestamp(), onupdate=datetime.now),
    Column('name', nullable=False),
    Column('structure_id', ForeignKey('structure.id'), nullable=False),
    UniqueConstraint('name', 'structure_id')
)

subject_table = Table(
    'subject',
    metadata,
    Column('id', Integer, default=Sequence('subject_seq'), primary_key=True),
    Column('created_at', DateTime, nullable=False, server_default=func.current_timestamp()),
    Column('edited_at', DateTime, nullable=False, server_default=func.current_timestamp(), onupdate=datetime.now),
    Column('name', Text, CheckConstraint('char_length(name) >= 1 AND char_length(name) <= 500'), nullable=False,
           unique=True),
)

subject_course = Table(
    'subject_course',
    metadata,
    Column('id', Integer, default=Sequence('subject_seq'), primary_key=True),
    Column('created_at', DateTime, nullable=False, server_default=func.current_timestamp()),
    Column('edited_at', DateTime, nullable=False, server_default=func.current_timestamp(), onupdate=datetime.now),
    Column('subject_id', ForeignKey('subject.id')),
    Column('course_id', ForeignKey('course.id'))
)

lesson_table = Table(
    'lesson',
    metadata,
    Column('id', Integer, default=Sequence('lesson_seq'), primary_key=True),
    Column('created_at', DateTime, nullable=False, server_default=func.current_timestamp()),
    Column('edited_at', DateTime, nullable=False, server_default=func.current_timestamp(), onupdate=datetime.now),
    Column('name', Text, CheckConstraint('1 <= char_length(name) AND char_length(name) <= 1000')),
    Column('description', Text, CheckConstraint('1 <= char_length(description) AND char_length(description) <= 5000')),
    Column('youtube_link', Text, CheckConstraint('char_length(youtube_link) >= 1 AND char_length(youtube_link) <= 500')),
    Column('date_start', Date),
    Column('time_start', Time),
    Column('time_finish', Time),
    Column('text', JSONB),
    Column('is_published', Boolean, server_default=expression.false(), nullable=False),
    Column('subject_id', ForeignKey('subject.id')),
    Column('course_id', ForeignKey('course.id')),
    Column('homework_id', ForeignKey('homework.id')),
    CheckConstraint('time_finish IS NULL OR time_start < time_end')
)


lesson_file_table = Table(
    'lesson_file',
    metadata,
    Column('id', Integer, default=Sequence('lesson_file_seq'), primary_key=True),
    Column('created_at', DateTime, nullable=False, server_default=func.current_timestamp()),
    Column('edited_at', DateTime, nullable=False, server_default=func.current_timestamp(), onupdate=datetime.now),
    Column('lesson_id', ForeignKey('lesson.id'), nullable=False),
    Column('file_link', Text, CheckConstraint('char_length(file_link) >= 3 AND char_length(file_link) <= 500'),
           nullable=False),
)


homework_table = Table(
    'homework',
    metadata,
    Column('id', Integer, default=Sequence('homework_seq'), primary_key=True),
    Column('created_at', DateTime, nullable=False, server_default=func.current_timestamp()),
    Column('edited_at', DateTime, nullable=False, server_default=func.current_timestamp(), onupdate=datetime.now),
    Column('homework_type', CheckConstraint("homework_type IN ('test', 'without-answer')")),
    Column('homework_without_answer_id', ForeignKey('homework_without_answer.id')),
    Column('homework_test_id', ForeignKey('homework_test.id')),
    CheckConstraint('homework_without_answer_id IS NULL OR homework_test_id IS NULL')
)


homework_without_answer_table = Table(
    'homework_without_answer',
    metadata,
    Column('id', Integer, default=Sequence('homework_without_answer_seq'), primary_key=True),
    Column('created_at', DateTime, nullable=False, server_default=func.current_timestamp()),
    Column('edited_at', DateTime, nullable=False, server_default=func.current_timestamp(), onupdate=datetime.now),
    Column('question', JSONB)
)


homework_test_table = Table(
    'homework_test',
    metadata,
    Column('id', Integer, default=Sequence('homework_test_seq'), primary_key=True),
    Column('created_at', DateTime, nullable=False, server_default=func.current_timestamp()),
    Column('edited_at', DateTime, nullable=False, server_default=func.current_timestamp(), onupdate=datetime.now)
)


test_question_table = Table(
    'test_question',
    metadata,
    Column('id', Integer, default=Sequence('test_question_seq'), primary_key=True),
    Column('created_at', DateTime, nullable=False, server_default=func.current_timestamp()),
    Column('edited_at', DateTime, nullable=False, server_default=func.current_timestamp(), onupdate=datetime.now),
    Column('homework_test_id', ForeignKey('homework_test.id'), nullable=False),
    Column('name', Text),
    Column('description', JSONB),
    Column('answer_type', CheckConstraint("answer_type IN ('one', 'many', 'text')")),
    Column('count_attempts', SmallInteger)
)


prompt_table = Table(
    'prompt',
    Column('id', Integer, default=Sequence('test_question_seq'), primary_key=True),
    Column('created_at', DateTime, nullable=False, server_default=func.current_timestamp()),
    Column('edited_at', DateTime, nullable=False, server_default=func.current_timestamp(), onupdate=datetime.now),
    Column('test_question_id', ForeignKey('test_question.id')),
    Column('text', JSONB)
)


answer_variant_table = Table(
    'answer_variant',
    metadata,
    Column('id', Integer, default=Sequence('test_question_seq'), primary_key=True),
    Column('created_at', DateTime, nullable=False, server_default=func.current_timestamp()),
    Column('edited_at', DateTime, nullable=False, server_default=func.current_timestamp(), onupdate=datetime.now),
    Column('test_question_id', ForeignKey('test_question.id'), nullable=False),
    Column('text', Text),
    Column('is_right', nullable=False)
)
