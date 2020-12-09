"""empty message

Revision ID: a60d59e6abcd
Revises: 944c3b514095
Create Date: 2020-12-09 14:14:38.253085

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a60d59e6abcd'
down_revision = '944c3b514095'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assignments',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('assignment_file', sa.String(length=512), nullable=True),
    sa.Column('comment', sa.String(length=512), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('due_date', sa.DateTime(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_assignments_student_id'), 'assignments', ['student_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_assignments_student_id'), table_name='assignments')
    op.drop_table('assignments')
    # ### end Alembic commands ###
