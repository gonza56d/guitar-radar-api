from enum import Enum


class BridgeType(str, Enum):
    """Options for different types of bridges."""

    FIXED = 'Fixed'
    HEADLESS = 'Headless'
    VINTAGE_TREMOLO = 'Vintage Tremolo'
    TWO_POINT_TREMOLO = 'Two Point Tremolo'
    FOUR_POINT_TREMOLO = 'Four Point Tremolo'
    FLOATING_TREMOLO = 'Floating Tremolo'
    TUNE_O_MATIC = 'Tune O Matic'


class TunerType(str, Enum):
    """Options for different types of tuners."""

    REGULAR = 'Regular'
    OPEN_CORE = 'Open Core'
    LOCKING = 'Locking'


class PickupType(str, Enum):
    """Options for different types of pickups."""

    SINGLE_COIL = 'Single Coil'
    HUMBUCKER = 'Humbucker'
    P90 = 'P90'
    STACKED_HUMBUCKER = 'Stacked Humbucker'
    HOT_RAIL = 'Hot Rail Humbucker'


class PickupMagnetType(str, Enum):
    """Options for different types of pickup magnets."""

    ALNICO_1 = 'Alnico I'
    ALNICO_2 = 'Alnico II'
    ALNICO_3 = 'Alnico III'
    ALNICO_4 = 'Alnico IV'
    ALNICO_5 = 'Alnico V'
    ALNICO_8 = 'Alnico VIII'
    CERAMIC = 'Ceramic'


class NutType(str, Enum):
    """Options for different types of nuts."""

    BONE = 'Bone'
    IVORY = 'Ivory'
    TUSQ = 'Tusq'
    GRAPHITE = 'Graphite'
    METAL = 'Metal'
    LOCKING = 'Locking'


class ControlType(str, Enum):
    """Options for different types of controls."""

    THREE_WAY_BLADE = 'Three way blade'
    FIVE_WAY_BLADE = 'Five way blade'
    THREE_WAY_SWITCH = 'Three way switch'
    KILLSWITCH = 'Killswitch'
    TWO_WAY_MINISWITCH = 'Two way miniswitch'
    THREE_WAY_MINISWITCH = 'Three way miniswitch'
    VOLUME_KNOB = 'Volume knob'
    TONE_KNOB = 'Tone knob'
    VOLUME_KNOB_PUSH_PULL = 'Volume knob w/ push pull'
    VOLUME_KNOB_PUSH_PUSH = 'Volume knob w/ push push'
    TONE_KNOB_PUSH_PULL = 'Tone knob w/ push pull'
    TONE_KNOB_PUSH_PUSH = 'Tone knob w/ push push'
    ROTARY_SWITCH = 'Rotary switch'


class WoodType(str, Enum):
    """Options for different types of woods."""

    ALDER = 'Alder'
    ASH = 'Ash'
    BUBINGA = 'Bubinga'
    WENGE = 'Wenge'
    FLAMED_ASH = 'Flamed Ash'
    BASSWOOD = 'Basswood'
    MAHOGANY = 'Mahogany'
    MAPLE = 'Maple'
    FLAMED_MAPLE = 'Flamed Maple'
    QUILTED_MAPLE = 'Quilted Maple'
    ROASTED_MAPLE = 'Roasted Maple'
    ROSEWOOD = 'Rosewood'
    EBONY = 'Ebony'
    OTHER = 'Other'


class HeadstockType(str, Enum):
    """Options for different types of headstocks."""

    INLINE = 'Inline'
    THREE_X_THREE = '3x3'
    TWO_X_FOUR = '2x4'
    THREE_X_FOUR = '3x4'
    FOUR_X_FOUR = '4x4'
    HEADLESS = 'Headless'
    OTHER = 'Other'


class FretType(str, Enum):
    """Options for different types of headstocks."""

    FRETLESS = 'Fretless'
    VINTAGE = 'Vintage'
    MEDIUM_JUMBO = 'Medium Jumbo'
    JUMBO = 'Jumbo'
    X_JUMBO = 'Extra Jumbo'


class FretMaterialType(str, Enum):
    """Options for different types of headstocks."""

    BRASS = 'Brass'
    NICKEL = 'Nickel'
    HARD_NICKEL = 'Hard Nickel'
    STAINLESS_STEEL = 'Stainless Steel'


class ConstructionType(str, Enum):
    """Options for different types of construction methods."""

    BOLT_ON = 'Bolt On'
    SET_NECK = 'Set Neck'
    NECK_THRU = 'Neck Thru'
    SET_THRU = 'Set Thru'
    ONE_PIECE = 'One piece'
