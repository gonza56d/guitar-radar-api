"""creation_user

Revision ID: 6251391333ef
Revises: 8c54f414f231
Create Date: 2023-12-31 23:22:01.478017

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6251391333ef'
down_revision: Union[str, None] = '8c54f414f231'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('brands', sa.Column('user_id', sa.UUID(), nullable=False))
    op.create_foreign_key(None, 'brands', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.add_column('bridges', sa.Column('user_id', sa.UUID(), nullable=False))
    op.create_foreign_key(None, 'bridges', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.add_column('colors', sa.Column('user_id', sa.UUID(), nullable=False))
    op.create_foreign_key(None, 'colors', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'colors', type_='foreignkey')
    op.drop_column('colors', 'user_id')
    op.drop_constraint(None, 'bridges', type_='foreignkey')
    op.drop_column('bridges', 'user_id')
    op.drop_constraint(None, 'brands', type_='foreignkey')
    op.drop_column('brands', 'user_id')
    # ### end Alembic commands ###
