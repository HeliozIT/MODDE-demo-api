"""added relationship admin id and items fix

Revision ID: 7f6b29ea7413
Revises: a527fa16d168
Create Date: 2024-08-19 20:50:30.588042

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7f6b29ea7413'
down_revision: Union[str, None] = 'a527fa16d168'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('added_by', sa.Integer(), server_default='2', nullable=False))
    op.create_foreign_key(None, 'items', 'admins', ['added_by'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'items', type_='foreignkey')
    op.drop_column('items', 'added_by')
    # ### end Alembic commands ###
