"""empty message

Revision ID: 0d458fe9d790
Revises: 503fd538d861
Create Date: 2024-07-05 20:29:11.706032

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '0d458fe9d790'
down_revision: Union[str, None] = '503fd538d861'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hotels')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hotels',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('location', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('services', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=False),
    sa.Column('rooms_quantity', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('image_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='hotels_pkey')
    )
    # ### end Alembic commands ###
