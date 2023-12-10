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
