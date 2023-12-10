from uuid import uuid4

from sqlalchemy import (
    Column,
    Enum,
    ForeignKey,
    Integer,
    String,
    Table
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import registry, relationship

from app.core.models import guitars


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
    get_name_column(),
    Column(
        'type',
        Enum(
            'FIXED', 'HEADLESS', 'VINTAGE_TREMOLO', 'TWO_POINT_TREMOLO', 'FOUR_POINT_TREMOLO',
            'FLOATING_TREMOLO', 'TUNE_O_MATIC',
            name='bridge_type',
            create_type=False
        )
    )
)


bridge_table = Table(
    'bridges',
    mapper_registry.metadata,
    *get_branded_component_columns(),

)

bridge_color_table = Table(
    'bridges_colors',
    mapper_registry.metadata,
    Column('color_id', ForeignKey('colors.id'), primary_key=True),
    Column('bridge_id', ForeignKey('bridges.id'), primary_key=True),
)

mapper_registry.map_imperatively(guitars.Brand, brand_table)
mapper_registry.map_imperatively(
    guitars.Bridge,
    bridge_table,
    properties={
        'brand': relationship(guitars.Brand),
        'colors': relationship(guitars.Color, secondary=bridge_color_table)
    }
)
mapper_registry.map_imperatively(guitars.Color, color_table)
