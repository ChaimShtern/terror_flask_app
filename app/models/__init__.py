from sqlalchemy.orm import declarative_base

Base = declarative_base()


from .attack_model import Attack
from .casualty_model import Casualty
from .group_model import Group
from .hostage_situation_model import HostageSituation
from .location_model import Location
from .property_dmage_model import PropertyDamage
from .weapon_model import Weapon
