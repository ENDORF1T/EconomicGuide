"""Add field for link on file with text

Revision ID: 47650f61247e
Revises: b3c8bd616e43
Create Date: 2024-03-28 19:57:16.213436

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '47650f61247e'
down_revision: Union[str, None] = 'b3c8bd616e43'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('information', sa.Column('text_link_on_file', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('information', 'text_link_on_file')
    # ### end Alembic commands ###