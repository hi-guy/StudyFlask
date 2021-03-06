"""empty message

Revision ID: 01725af88a9d
Revises: 3d7fea6d2dc5
Create Date: 2018-05-02 16:29:34.418469

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '01725af88a9d'
down_revision = '3d7fea6d2dc5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('user_avatar', sa.String(length=64), nullable=True))
    op.drop_column('user', 'avatar1')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('avatar1', mysql.VARCHAR(collation='utf8_bin', length=64), nullable=True))
    op.drop_column('user', 'user_avatar')
    # ### end Alembic commands ###
