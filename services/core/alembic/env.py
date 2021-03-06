import os
from logging.config import fileConfig

from alembic import context
from sqlalchemy import create_engine

from src.schema.meta import metadata

config = context.config

fileConfig(config.config_file_name)

target_metadata = metadata


def get_url():
    return "postgresql://%s:%s@%s/%s" % (
        os.getenv("PODGOTOVKA_DB_USER", "postgres"),
        os.getenv("PODGOTOVKA_DB_PASSWORD", "root"),
        os.getenv("PODGOTOVKA_DB_HOST", "127.0.0.1"),
        os.getenv("PODGOTOVKA_PRIMARY_DB_NAME", "podgotovka_primary"),
    )


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = create_engine(get_url())
    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
