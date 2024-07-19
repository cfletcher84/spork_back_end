"""empty message

Revision ID: c7feae971e82
Revises: 402dc7bf57dd
Create Date: 2024-07-19 14:08:36.878349

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7feae971e82'
down_revision = '402dc7bf57dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=300), nullable=False),
    sa.Column('password', sa.String(length=500), nullable=False),
    sa.Column('spoons', sa.Integer(), nullable=False),
    sa.Column('profile_pic', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('flares',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('flare', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('task', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.Column('date', sa.String(length=20), nullable=True),
    sa.Column('spoons_needed', sa.Integer(), nullable=False),
    sa.Column('duration', sa.String(length=100), nullable=False),
    sa.Column('time_of_day', sa.String(length=100), nullable=False),
    sa.Column('icon', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tasks')
    op.drop_table('flares')
    op.drop_table('users')
    # ### end Alembic commands ###
