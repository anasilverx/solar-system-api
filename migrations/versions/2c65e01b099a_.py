"""empty message

Revision ID: 2c65e01b099a
Revises: 071ddf6f6504
Create Date: 2023-05-03 19:40:54.992412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c65e01b099a'
down_revision = '071ddf6f6504'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('description', sa.String(length=80), nullable=True),
    sa.Column('species', sa.String(length=80), nullable=True),
    sa.Column('weather', sa.String(length=80), nullable=True),
    sa.Column('distance_to_sun', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    # ### end Alembic commands ###