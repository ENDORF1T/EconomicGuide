"""Add field update_at

Revision ID: 38a5a6d43053
Revises: a6c802128955
Create Date: 2024-03-29 10:15:43.226944

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '38a5a6d43053'
down_revision: Union[str, None] = 'a6c802128955'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('information', sa.Column('update_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('information', 'update_at')
    # ### end Alembic commands ###
