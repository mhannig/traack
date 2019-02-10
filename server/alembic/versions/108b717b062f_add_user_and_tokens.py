"""add user and tokens

Revision ID: 108b717b062f
Revises: 3c183162b40e
Create Date: 2019-02-10 12:37:22.572752

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '108b717b062f'
down_revision = '3c183162b40e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auth_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password_hash', sa.String(length=80), nullable=True),
    sa.Column('api_key', sa.String(length=16), nullable=True),
    sa.Column('api_secret', sa.String(length=86), nullable=True),
    sa.Column('first_name', sa.String(length=30), nullable=True),
    sa.Column('last_name', sa.String(length=30), nullable=True),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('auth_token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('bearer', sa.String(length=86), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('issued_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('expires_at', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('bearer')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('auth_token')
    op.drop_table('auth_user')
    # ### end Alembic commands ###
