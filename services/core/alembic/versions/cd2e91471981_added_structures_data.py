"""Added structures data

Revision ID: cd2e91471981
Revises: 85e9be882057
Create Date: 2021-06-11 15:43:47.934555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd2e91471981'
down_revision = '85e9be882057'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
        INSERT INTO structure(id, name) VALUES (1, 'primary-school');
        INSERT INTO structure(id, name) VALUES (2, 'school');
        INSERT INTO structure(id, name) VALUES (3, 'high-school');
    """)


def downgrade():
    op.execute("""
        DELETE
        FROM
            structure
        WHERE
            id IN (1, 2, 3)
    """)
