"""empty message

Revision ID: 246317403df3
Revises: acde149bc032
Create Date: 2018-03-17 22:16:34.424586

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '246317403df3'
down_revision = 'acde149bc032'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('category_slug', sa.String(length=140), nullable=True))
    op.drop_index('slug', table_name='category')
    op.create_unique_constraint(None, 'category', ['category_slug'])
    op.drop_column('category', 'slug')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('slug', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True))
    op.drop_constraint(None, 'category', type_='unique')
    op.create_index('slug', 'category', ['slug'], unique=True)
    op.drop_column('category', 'category_slug')
    # ### end Alembic commands ###
