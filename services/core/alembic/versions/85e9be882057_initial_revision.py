"""initial_revision

Revision ID: 85e9be882057
Revises: 
Create Date: 2021-06-10 16:03:10.590770

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '85e9be882057'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('account_student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('edited_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('email', sa.Text(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('last_name', sa.Text(), nullable=True),
    sa.Column('middle_name', sa.Text(), nullable=True),
    sa.Column('photo_link', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('hash_password', sa.Text(), nullable=True),
    sa.Column('vk_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__account_student')),
    sa.UniqueConstraint('email', name=op.f('uq__account_student__email')),
    sa.UniqueConstraint('vk_id', name=op.f('uq__account_student__vk_id'))
    )
    op.create_table('account_teacher',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('edited_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('email', sa.Text(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('last_name', sa.Text(), nullable=True),
    sa.Column('middle_name', sa.Text(), nullable=True),
    sa.Column('photo_link', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('hash_password', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__account_teacher')),
    sa.UniqueConstraint('email', name=op.f('uq__account_teacher__email'))
    )
    op.create_table('homework_test',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('edited_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__homework_test'))
    )
    op.create_table('homework_without_answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('edited_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('question', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__homework_without_answer'))
    )
    op.create_table('structure',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__structure')),
    sa.UniqueConstraint('name', name=op.f('uq__structure__name'))
    )
    op.create_table('subject',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('edited_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__subject')),
    sa.UniqueConstraint('name', name=op.f('uq__subject__name'))
    )
    op.create_table('course',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('edited_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('structure_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['structure_id'], ['structure.id'], name=op.f('fk__course__structure_id__structure')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__course')),
    sa.UniqueConstraint('name', 'structure_id', name=op.f('uq__course__name_structure_id'))
    )
    op.create_table('homework',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('edited_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('homework_type', sa.Text(), nullable=True),
    sa.Column('homework_without_answer_id', sa.Integer(), nullable=True),
    sa.Column('homework_test_id', sa.Integer(), nullable=True),
    sa.CheckConstraint('homework_without_answer_id IS NULL OR homework_test_id IS NULL', name=op.f('ck__homework__')),
    sa.ForeignKeyConstraint(['homework_test_id'], ['homework_test.id'], name=op.f('fk__homework__homework_test_id__homework_test'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['homework_without_answer_id'], ['homework_without_answer.id'], name=op.f('fk__homework__homework_without_answer_id__homework_without_answer'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__homework'))
    )
    op.create_table('test_question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('edited_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('homework_test_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('answer_type', sa.Text(), nullable=True),
    sa.Column('count_attempts', sa.SmallInteger(), nullable=True),
    sa.ForeignKeyConstraint(['homework_test_id'], ['homework_test.id'], name=op.f('fk__test_question__homework_test_id__homework_test'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__test_question'))
    )
    op.create_table('answer_variant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('edited_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('test_question_id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('is_right', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['test_question_id'], ['test_question.id'], name=op.f('fk__answer_variant__test_question_id__test_question'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__answer_variant'))
    )
    op.create_table('lesson',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('edited_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('youtube_link', sa.Text(), nullable=True),
    sa.Column('time_start', sa.DateTime(), nullable=True),
    sa.Column('time_finish', sa.Time(), nullable=True),
    sa.Column('text', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('is_published', sa.Boolean(), server_default=sa.text('false'), nullable=False),
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('homework_id', sa.Integer(), nullable=True),
    sa.Column('account_teacher_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['account_teacher_id'], ['account_teacher.id'], name=op.f('fk__lesson__account_teacher_id__account_teacher'), ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], name=op.f('fk__lesson__course_id__course'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['homework_id'], ['homework.id'], name=op.f('fk__lesson__homework_id__homework'), ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], name=op.f('fk__lesson__subject_id__subject'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__lesson'))
    )
    op.create_table('prompt',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('edited_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('test_question_id', sa.Integer(), nullable=True),
    sa.Column('text', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.ForeignKeyConstraint(['test_question_id'], ['test_question.id'], name=op.f('fk__prompt__test_question_id__test_question'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__prompt'))
    )
    op.create_table('subject_course',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('edited_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], name=op.f('fk__subject_course__course_id__course'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], name=op.f('fk__subject_course__subject_id__subject'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__subject_course')),
    sa.UniqueConstraint('subject_id', 'course_id', name=op.f('uq__subject_course__subject_id_course_id'))
    )
    op.create_table('subject_course_subscription',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('edited_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('account_student_id', sa.Integer(), nullable=False),
    sa.Column('subject_id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['account_student_id'], ['account_student.id'], name=op.f('fk__subject_course_subscription__account_student_id__account_student'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], name=op.f('fk__subject_course_subscription__course_id__course'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], name=op.f('fk__subject_course_subscription__subject_id__subject'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__subject_course_subscription')),
    sa.UniqueConstraint('account_student_id', 'subject_id', 'course_id', name=op.f('uq__subject_course_subscription__account_student_id_subject_id_course_id'))
    )
    op.create_table('lesson_file',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('edited_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('lesson_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('file_link', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['lesson_id'], ['lesson.id'], name=op.f('fk__lesson_file__lesson_id__lesson'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__lesson_file'))
    )
    op.create_table('lesson_view',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('edited_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('lesson_id', sa.Integer(), nullable=False),
    sa.Column('account_student_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['account_student_id'], ['account_student.id'], name=op.f('fk__lesson_view__account_student_id__account_student'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['lesson_id'], ['lesson.id'], name=op.f('fk__lesson_view__lesson_id__lesson'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__lesson_view'))
    )


def downgrade():
    op.drop_table('lesson_view')
    op.drop_table('lesson_file')
    op.drop_table('subject_course_subscription')
    op.drop_table('subject_course')
    op.drop_table('prompt')
    op.drop_table('lesson')
    op.drop_table('answer_variant')
    op.drop_table('test_question')
    op.drop_table('homework')
    op.drop_table('course')
    op.drop_table('subject')
    op.drop_table('structure')
    op.drop_table('homework_without_answer')
    op.drop_table('homework_test')
    op.drop_table('account_teacher')
    op.drop_table('account_student')
