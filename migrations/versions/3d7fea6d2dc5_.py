"""empty message

Revision ID: 3d7fea6d2dc5
Revises: cf22696439ce
Create Date: 2018-05-02 16:29:16.124584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d7fea6d2dc5'
down_revision = 'cf22696439ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('avatar1', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'avatar1')
    # ### end Alembic commands ###
