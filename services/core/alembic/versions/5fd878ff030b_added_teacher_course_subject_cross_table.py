"""added teacher course subject cross table

Revision ID: 5fd878ff030b
Revises: 85e9be882057
Create Date: 2021-06-11 14:07:25.743124

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5fd878ff030b'
down_revision = 'cd2e91471981'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('subject_course_lead',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('edited_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('account_teacher_id', sa.Integer(), nullable=False),
    sa.Column('subject_course_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['account_teacher_id'], ['account_teacher.id'], name=op.f('fk__subject_course_lead__account_teacher_id__account_teacher'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['subject_course_id'], ['subject_course.id'], name=op.f('fk__subject_course_lead__subject_course_id__subject_course'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__subject_course_lead')),
    sa.UniqueConstraint('account_teacher_id', 'subject_course_id', name=op.f('uq__subject_course_lead__account_teacher_id_subject_course_id'))
    )
    op.add_column('subject_course_subscription', sa.Column('subject_course_id', sa.Integer(), nullable=False))
    op.drop_constraint('uq__subject_course_subscription__account_student_id_sub_56d3', 'subject_course_subscription', type_='unique')
    op.create_unique_constraint(op.f('uq__subject_course_subscription__account_student_id_subject_course_id'), 'subject_course_subscription', ['account_student_id', 'subject_course_id'])
    op.drop_constraint('fk__subject_course_subscription__subject_id__subject', 'subject_course_subscription', type_='foreignkey')
    op.drop_constraint('fk__subject_course_subscription__course_id__course', 'subject_course_subscription', type_='foreignkey')
    op.create_foreign_key(op.f('fk__subject_course_subscription__subject_course_id__subject_course'), 'subject_course_subscription', 'subject_course', ['subject_course_id'], ['id'], ondelete='CASCADE')
    op.drop_column('subject_course_subscription', 'subject_id')
    op.drop_column('subject_course_subscription', 'course_id')


def downgrade():
    op.add_column('subject_course_subscription', sa.Column('course_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('subject_course_subscription', sa.Column('subject_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(op.f('fk__subject_course_subscription__subject_course_id__subject_course'), 'subject_course_subscription', type_='foreignkey')
    op.create_foreign_key('fk__subject_course_subscription__course_id__course', 'subject_course_subscription', 'course', ['course_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('fk__subject_course_subscription__subject_id__subject', 'subject_course_subscription', 'subject', ['subject_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(op.f('uq__subject_course_subscription__account_student_id_subject_course_id'), 'subject_course_subscription', type_='unique')
    op.create_unique_constraint('uq__subject_course_subscription__account_student_id_sub_56d3', 'subject_course_subscription', ['account_student_id', 'subject_id', 'course_id'])
    op.drop_column('subject_course_subscription', 'subject_course_id')
    op.drop_table('subject_course_lead')
