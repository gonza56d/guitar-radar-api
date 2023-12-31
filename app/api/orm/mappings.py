from uuid import uuid4

from sqlalchemy import (
    Column,
    Date,
    Enum,
    ForeignKey,
    Integer,
    String,
    Table
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import registry, relationship

from app.core.models import auth, guitars, users


mapper_registry = registry()


def get_id_column():
    return Column('id', UUID(as_uuid=True), primary_key=True, default=uuid4)


def get_name_column():
    return Column('name', String(100), unique=True)


def get_branded_component_columns() -> list[Column]:
    return [
        get_id_column(),
        Column('brand_id', UUID(as_uuid=True), ForeignKey('brands.id', ondelete='CASCADE'), nullable=False),
        get_name_column(),
        Column('year_of_introduction', Integer, nullable=True),
        Column('user_id', UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
    ]


brand_table = Table(
    'brands',
    mapper_registry.metadata,
    get_id_column(),
    get_name_column(),
    Column('founded_in', Integer, nullable=True),
    Column('user_id', UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
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
    ),
    Column('user_id', UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
)


bridge_table = Table(
    'bridges',
    mapper_registry.metadata,
    *get_branded_component_columns(),
)

bridge_color_table = Table(
    'bridges_colors',
    mapper_registry.metadata,
    Column('color_id', ForeignKey('colors.id', ondelete='CASCADE'), primary_key=True),
    Column('bridge_id', ForeignKey('bridges.id', ondelete='CASCADE'), primary_key=True),
)


users_table = Table(
    'users',
    mapper_registry.metadata,
    get_id_column(),
    Column('first_name', String, nullable=False),
    Column('last_name', String, nullable=False),
    Column('email', String, nullable=False),
    Column('birth', Date, nullable=False),
)


auth_table = Table(
    'auth',
    mapper_registry.metadata,
    get_id_column(),
    Column('user_id', UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
    Column('password', String, nullable=False)
)


mapper_registry.map_imperatively(users.User, users_table)
mapper_registry.map_imperatively(auth.Auth, auth_table)
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
