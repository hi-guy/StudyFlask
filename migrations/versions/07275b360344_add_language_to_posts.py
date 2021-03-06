"""add language to posts

Revision ID: 07275b360344
Revises: 071fbc0dba9e
Create Date: 2018-04-25 10:41:50.990794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07275b360344'
down_revision = '071fbc0dba9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
