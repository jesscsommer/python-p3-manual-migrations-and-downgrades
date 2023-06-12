"""Renaming name to first_name

Revision ID: b3737b8fbf1a
Revises: a9aea5d3cdfc
Create Date: 2023-06-12 09:35:15.631046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3737b8fbf1a'
down_revision = 'a9aea5d3cdfc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars', 'name', new_column_name='first_name')


def downgrade() -> None:
    op.alter_column('scholars', 'first_name', new_column_name='name')
