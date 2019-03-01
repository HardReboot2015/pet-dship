"""empty message

Revision ID: 011026aef993
Revises: 01f44acc7779
Create Date: 2019-02-16 21:44:13.097325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '011026aef993'
down_revision = '01f44acc7779'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('color',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('size', sa.String(length=32), nullable=False),
    sa.Column('payed', sa.Boolean(), nullable=True),
    sa.Column('id_product', sa.Integer(), nullable=True),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_product'], ['product.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('items')
    op.drop_table('color')
    op.drop_table('category')
    # ### end Alembic commands ###
