"""init

Revision ID: ccfd3fdb4ad3
Revises: 
Create Date: 2020-09-22 08:49:33.415603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccfd3fdb4ad3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item_type',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('location_type',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('player_class',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('location',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('locationNum', sa.String(length=10), nullable=True),
    sa.Column('locationType', sa.Integer(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['locationType'], ['location_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('player',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('classId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['classId'], ['player_class.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('item',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('itemType', sa.Integer(), nullable=True),
    sa.Column('quality', sa.Integer(), nullable=True),
    sa.Column('owner', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['itemType'], ['item_type.id'], ),
    sa.ForeignKeyConstraint(['owner'], ['player.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('message',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('playerFrom', sa.Integer(), nullable=True),
    sa.Column('playerTo', sa.Integer(), nullable=True),
    sa.Column('messageText', sa.String(length=1000), nullable=True),
    sa.ForeignKeyConstraint(['playerFrom'], ['player.id'], ),
    sa.ForeignKeyConstraint(['playerTo'], ['player.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('message')
    op.drop_table('item')
    op.drop_table('player')
    op.drop_table('location')
    op.drop_table('player_class')
    op.drop_table('location_type')
    op.drop_table('item_type')
    # ### end Alembic commands ###