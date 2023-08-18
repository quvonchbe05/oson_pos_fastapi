"""added basket

Revision ID: 14294ced0a9b
Revises: 9e5ced7acf04
Create Date: 2023-08-18 08:54:29.623673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14294ced0a9b'
down_revision = '9e5ced7acf04'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('basket',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Integer(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.Column('price', sa.String(length=155), nullable=True),
    sa.Column('total_price', sa.String(length=155), nullable=True),
    sa.Column('user', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['name'], ['product.id'], ),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('basket')
    # ### end Alembic commands ###