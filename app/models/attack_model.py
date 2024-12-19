from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.models import Base
from app.models.attack_group_bridge_model import attack_group_association


class Attack(Base):
    __tablename__ = 'attacks'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    year = Column(Integer)
    month = Column(Integer)
    day = Column(Integer)

    attack_type1 = Column(String)
    attack_type2 = Column(String)
    attack_type3 = Column(String)

    summary = Column(Text)
    additional_notes = Column(Text)
    source1 = Column(Text)
    source2 = Column(Text)
    source3 = Column(Text)

    target_type1 = Column(String)
    target_type2 = Column(String)
    target_type3 = Column(String)

    location_id = Column(Integer, ForeignKey("locations.id"))
    location = relationship("Location", back_populates="attacks")

    weapons = relationship("Weapon", back_populates="attack")
    casualties = relationship("Casualty", back_populates="attack")
    property_damage = relationship("PropertyDamage", back_populates="attack")
    hostage_situation = relationship("HostageSituation", back_populates="attack")
    groups = relationship("Group", secondary=attack_group_association, back_populates="attacks")
