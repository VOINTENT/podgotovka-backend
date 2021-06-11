"""Added lesson status

Revision ID: aa1296e1138c
Revises: cd2e91471981
Create Date: 2021-06-11 18:02:42.213037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa1296e1138c'
down_revision = 'cd2e91471981'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('lesson', sa.Column('status', sa.Text(), server_default=sa.text("'draft'"), nullable=False))
    op.drop_column('lesson', 'is_published')


def downgrade():
    op.add_column('lesson', sa.Column('is_published', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False))
    op.drop_column('lesson', 'status')
