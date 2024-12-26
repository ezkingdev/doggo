"""Add color field to Note

Revision ID: 6c82f7671f35
Revises: 03908b96e563
Create Date: 2024-05-15 02:48:49.595295

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6c82f7671f35'
down_revision: Union[str, None] = '03908b96e563'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
