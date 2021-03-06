"""empty message

Revision ID: c5f39c13dc84
Revises: c0ffb4be2e9c
Create Date: 2018-03-13 11:50:34.783706

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5f39c13dc84'
down_revision = 'c0ffb4be2e9c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('short_title', sa.String(length=30), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'short_title')
    # ### end Alembic commands ###
