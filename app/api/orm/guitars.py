from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import registry


mapper_registry = registry()


def get_id_column():
    return Column('id', UUID(as_uuid=True), primary_key=True, default=uuid4)


def get_name_column():
    return Column('name', String(100), unique=True)


def get_branded_component_columns() -> list[Column]:
    return [
        get_id_column(),
        Column('brand_id', UUID(as_uuid=True), ForeignKey('brands.id')),
        get_name_column(),
        Column('year_of_introduction', Integer, nullable=True),
    ]


brand_table = Table(
    'brands',
    mapper_registry.metadata,
    get_id_column(),
    get_name_column(),
    Column('founded_in', Integer, nullable=True)
)


color_table = Table(
    'colors',
    mapper_registry.metadata,
    get_id_column(),
    get_name_column()
)


user_table = Table(
    'users',
    mapper_registry.metadata,
    #body: Body,
    #neck: Neck,
    #construction_method: ConstructionType,
    Column('number_of_strings', Integer),
    # nut_type: NutType,
    # is_nut_compensated: bool,
    # number_of_frets: int,
    # frets_type: FretType,
    # frets_material: FretMaterialType | None = None,
    # headstock_type: HeadstockType,
    # tuners: Tuner,
    # bridge: Bridge,
    # bridge_pickup: Pickup | None = None,
    # middle_pickup: Pickup | None = None,
    # neck_pickup: Pickup | None = None,
    # has_piezo: bool = False,
    # controls: list[ControlType],
)
