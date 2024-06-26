"""Create table

Revision ID: 4bda167d20b8
Revises: 
Create Date: 2024-03-28 18:58:40.312319

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4bda167d20b8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('information',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title_article', sa.String(), nullable=False),
    sa.Column('link_on_photo', sa.String(), nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('information')
    # ### end Alembic commands ###
