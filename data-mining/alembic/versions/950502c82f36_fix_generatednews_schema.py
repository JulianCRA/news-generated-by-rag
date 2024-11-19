"""Fix GeneratedNews schema

Revision ID: 950502c82f36
Revises: cfbb661f8c72
Create Date: 2024-11-18 22:04:03.746156

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '950502c82f36'
down_revision: Union[str, None] = 'cfbb661f8c72'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('generated_news', sa.Column('section_id', sa.Integer(), nullable=False))
    op.drop_index('ix_generated_news_section', table_name='generated_news')
    op.create_index('ix_generated_news_section_id', 'generated_news', ['section_id'], unique=False)
    op.create_foreign_key(None, 'generated_news', 'sections', ['section_id'], ['id'])
    op.drop_column('generated_news', 'section')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('generated_news', sa.Column('section', mysql.VARCHAR(length=100), nullable=False))
    op.drop_constraint(None, 'generated_news', type_='foreignkey')
    op.drop_index('ix_generated_news_section_id', table_name='generated_news')
    op.create_index('ix_generated_news_section', 'generated_news', ['section'], unique=False)
    op.drop_column('generated_news', 'section_id')
    # ### end Alembic commands ###