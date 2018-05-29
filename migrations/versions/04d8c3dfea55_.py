"""empty message

Revision ID: 04d8c3dfea55
Revises: 246317403df3
Create Date: 2018-03-17 22:37:43.430396

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '04d8c3dfea55'
down_revision = '246317403df3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('post_slug', sa.String(length=140), nullable=True))
    op.drop_index('slug', table_name='post')
    op.create_unique_constraint(None, 'post', ['post_slug'])
    op.drop_column('post', 'slug')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('slug', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True))
    op.drop_constraint(None, 'post', type_='unique')
    op.create_index('slug', 'post', ['slug'], unique=True)
    op.drop_column('post', 'post_slug')
    # ### end Alembic commands ###
