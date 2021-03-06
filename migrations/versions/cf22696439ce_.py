"""empty message

Revision ID: cf22696439ce
Revises: 33c43892786b
Create Date: 2018-05-02 16:24:38.465291

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cf22696439ce'
down_revision = '33c43892786b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'logo')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('logo', mysql.VARCHAR(collation='utf8_bin', length=64), nullable=True))
    # ### end Alembic commands ###
