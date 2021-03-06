"""followers

Revision ID: 378e16f0aa97
Revises: 6bfe2503d9b2
Create Date: 2018-12-06 14:18:41.634519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '378e16f0aa97'
down_revision = '6bfe2503d9b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
