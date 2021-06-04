"""Account teacher table

Revision ID: d1deddcb7120
Revises: 
Create Date: 2021-06-04 15:33:01.586004

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'd1deddcb7120'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'account_teacher',
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


def downgrade():
    op.drop_table('account_teacher')
