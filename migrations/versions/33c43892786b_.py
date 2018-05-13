"""empty message

Revision ID: 33c43892786b
Revises: 4206a8775267
Create Date: 2018-05-02 16:24:12.028443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33c43892786b'
down_revision = '4206a8775267'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('logo', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'logo')
    # ### end Alembic commands ###