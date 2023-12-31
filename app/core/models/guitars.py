from dataclasses import dataclass, field
from uuid import UUID

from .enums import *


@dataclass(kw_only=True)
class Color:

    id: UUID
    name: str
    user_id: UUID


@dataclass(kw_only=True)
class Brand:

    id: UUID
    name: str
    founded_in: int | None = None
    user_id: UUID


@dataclass(kw_only=True)
class BrandedComponent:

    id: UUID
    user_id: UUID
    brand: Brand
    name: str
    year_of_introduction: int | None = None
    colors: list[Color] = field(default=list)


@dataclass(kw_only=True)
class Bridge(BrandedComponent):

    type: BridgeType


@dataclass(kw_only=True)
class Tuner(BrandedComponent):

    type: TunerType


@dataclass(kw_only=True)
class Pickup(BrandedComponent):

    type: PickupType
    magnet_type: PickupMagnetType
    is_active: bool
    is_covered: bool = False


@dataclass(kw_only=True)
class Body(BrandedComponent):

    core_wood: WoodType
    top_wood: WoodType
    back_wood: WoodType
    is_chambered: bool
    is_carved: bool
    binding_front: Color | None = None
    binding_back: Color | None = None


@dataclass(kw_only=True)
class Neck(BrandedComponent):

    woods: list[WoodType]
    pieces: int
    fretboard: WoodType | None = None

    @property
    def description(self) -> str:
        woods = self._get_woods_str()
        pieces_word = 'piece' if self.pieces == 1 else 'pieces'
        return f'{self.pieces} {pieces_word} neck of {woods.lower()}.'

    def _get_woods_str(self) -> str:
        woods_str = (
            ' and '.join(wood for wood in self.woods)
            if len(self.woods) == 2 else
            ', '.join(wood for wood in self.woods)
        )
        return self._get_fixed_comma(woods_str)

    def _get_fixed_comma(self, woods) -> str:
        if len(self.woods) > 2:
            last_comma_at = woods.rfind(',')
            woods = f'{woods[:last_comma_at]} and{woods[last_comma_at + 1:]}'
        return woods


@dataclass(kw_only=True)
class Guitar(BrandedComponent):

    body: Body
    neck: Neck
    construction_method: ConstructionType
    number_of_strings: int = 6
    nut_type: NutType
    is_nut_compensated: bool
    number_of_frets: int
    frets_type: FretType
    frets_material: FretMaterialType | None = None
    headstock_type: HeadstockType
    tuners: Tuner
    bridge: Bridge
    bridge_pickup: Pickup | None = None
    middle_pickup: Pickup | None = None
    neck_pickup: Pickup | None = None
    has_piezo: bool = False
    controls: list[ControlType]

    @property
    def colors(self) -> list[Color]:
        """Overriden. Returns the color of the body of the guitar."""
        return self.body.colors

    @property
    def hardware_color_str(self) -> str:
        """
        Get readable message for the hardware color(s).

        Example: 'Gold, Black.'
        """
        hardware_colors = {color.value for color in {element.colors for element in self.hardware}}
        return ', '.join(hardware_colors)

    @property
    def hardware(self) -> list[BrandedComponent]:
        return [self.bridge, self.tuners]

    @property
    def controls_str(self) -> str:
        """
        Get readable message for the list of controls of the guitar.

        Example: 'x2 Volume knob, x1 Tone knob, x1 Three way blade.'
        """
        controls_dict = self._get_controls_dict()
        return ', '.join(
            f'x{k} {v}' for k, v in controls_dict.items()
        )

    def _get_controls_dict(self) -> dict[str, int]:
        controls_str = [control.value for control in self.controls]
        controls_dict = {}
        for control in controls_str:
            try:
                controls_dict[control] += 1
            except KeyError:
                controls_dict[control] = 1
        return controls_dict
