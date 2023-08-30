from typing import Any

from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy.orm import DeclarativeBase


def add_row_to_table(database: SQLAlchemy, table: Any, **kwargs: Any) -> None:
    """Add a row to a table in the database.

    Args:
        database (SQLAlchemy): SQLAlchemy object.
        table (Any): Table in the database.
        **kwargs (Any): Arguments to be added to the table.
    """
    new_row = table(**kwargs)
    database.session.add(new_row)
    database.session.commit()


def delete_row_from_table(database: SQLAlchemy, table: Any, id: Any) -> None:
    """Delete a row to a table in the database.

    Args:
        database (SQLAlchemy): SQLAlchemy object.
        table (Any): Table in the database.
        id (Any): id to be delete to the table.
    """
    target_row: Any = table.query.get_or_404(id)
    database.session.delete(target_row)
    database.session.commit()
