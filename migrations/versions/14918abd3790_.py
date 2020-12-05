"""empty message

Revision ID: 14918abd3790
Revises: 
Create Date: 2020-12-05 14:57:06.110390

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14918abd3790'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('gender', sa.Enum('MALE', 'FEMALE', 'OTHER', name='gendertype'), nullable=False),
    sa.Column('student_class', sa.String(length=32), nullable=False),
    sa.Column('mobile', sa.String(length=32), nullable=False),
    sa.Column('father_name', sa.String(length=256), nullable=True),
    sa.Column('address', sa.String(length=512), nullable=False),
    sa.Column('tc', sa.String(length=512), nullable=True),
    sa.Column('photo', sa.String(length=512), nullable=True),
    sa.Column('migration', sa.String(length=512), nullable=True),
    sa.Column('dob', sa.Date(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('attendance',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('status', sa.Enum('ABSENT', 'PRESENT', 'HALF_DAY', name='status'), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_attendance_student_id'), 'attendance', ['student_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_attendance_student_id'), table_name='attendance')
    op.drop_table('attendance')
    op.drop_table('students')
    # ### end Alembic commands ###
