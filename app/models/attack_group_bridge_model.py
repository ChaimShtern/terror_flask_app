from sqlalchemy import Table, Column, Integer, ForeignKey
from app.models import Base

attack_group_association = Table(
    'attack_group_association',
    Base.metadata,
    Column('attack_id', Integer, ForeignKey('attacks.id'), primary_key=True),
    Column('group_id', Integer, ForeignKey('groups.id'), primary_key=True)
)