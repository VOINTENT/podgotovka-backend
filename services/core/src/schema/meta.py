from datetime import datetime

import sqlalchemy
from sqlalchemy import Table, Column, Integer, Sequence, DateTime, func, Text, CheckConstraint

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
    Column('id', Integer, default=Sequence('account_teacher_seq'), primary_key=True, nullable=False),
    Column('created_at', DateTime, nullable=False, server_default=func.current_timestamp()),
    Column('edited_at', DateTime, nullable=False, server_default=func.current_timestamp(), onupdate=datetime.now),
    Column('email', Text, CheckConstraint('char_length(email) >= 4 AND char_length(email) <= 100'), nullable=False, unique=True),
    Column('name', Text, CheckConstraint('char_length(name) >= 1 AND char_length(email) <= 100'), nullable=False),
    Column('last_name', Text, CheckConstraint('char_length(last_name) >= 1 AND char_length(last_name) <= 100')),
    Column('middle_name', Text, CheckConstraint('char_length(middle_name) >= 1 AND char_length(middle_name) <= 100')),
    Column('photo_link', Text, CheckConstraint('char_length(photo_link) >= 1 AND char_length(photo_link) <= 1000')),
    Column('description', Text, CheckConstraint('char_length(description) >= 1 AND char_length(description) <= 5000')),
    Column('hash_password', Text, CheckConstraint('char_length(hash_password) >= 1 AND char_length(hash_password) <= 500'), nullable=False)
)
