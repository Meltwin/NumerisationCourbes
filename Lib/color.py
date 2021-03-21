import enum
from typing import Tuple
import copy


def hex_format(substr: str) -> str:
    if len(substr) == 1:
        return "0"+substr
    return substr


class RGBAColor:
    """
    Represents a rgba color
    """
    def __init__(self, red: int = 0, green: int = 0, blue: int = 0, alpha: float = 1., nbits: int = 8):
        self._red = red
        self._green = green
        self._blue = blue
        self._bits = (nbits, 2 ** nbits)
        self._alpha = alpha

    # Getters
    def set_bit(self, nb_bit: int) -> None: self._bits = (nb_bit, 2**nb_bit)
    def get_bit(self) -> int: return self._bits[0]

    ###################################
    #           Color getter
    ###################################
    def get_rgba(self) -> Tuple[int, int, int, float]:
        """
        :return: (r, g, b, alpha) with r, g and b in [0, 2**nbits] and alpha in [0, 1]
        """
        return self._red, self._green, self._blue, self._alpha

    def get_rgba_reduce(self) -> Tuple[float, float, float, float]:
        """
        :return: (r, g, b, alpha) with r, g, b and alpha in [0,1]
        """
        tr = self._red / self._bits[1]
        tg = self._green / self._bits[1]
        tb = self._blue / self._bits[1]
        return tr, tg, tb, self._alpha

    def get_rgb(self) -> Tuple[int, int, int]:
        """
        :return: (r, g, b) with r, g and b in [0, 2**nbits]
        """
        return self._red, self._green, self._blue

    def get_rgb_reduce(self) -> Tuple[float, float, float]:
        """
        :return: (r, g, b) with r, g, b in [0,1]
        """
        tr = self._red / self._bits[1]
        tg = self._green / self._bits[1]
        tb = self._blue / self._bits[1]
        return tr, tg, tb

    def get_hex(self) -> str:
        """
        Return the hex code for the color
        :return:
        """
        return f"#{hex_format(hex(self._red)[2:])}{hex_format(hex(self._green)[2:])}{hex_format(hex(self._blue)[2:])}"

    ###################################
    #             Import
    ###################################
    def from_hex(self, hex_string: str) -> "RGBAColor":
        assert len(str) != 7
        self._red = int(hex_string[1] + hex_string[2], 16)
        self._green = int(hex_string[3] + hex_string[4], 16)
        self._blue = int(hex_string[5] + hex_string[6], 16)
        self._alpha = 1.
        return self

    def from_rgba(self, red: int, green: int, blue: int, alpha: float = 1.) -> "RGBAColor":
        self._red = red
        self._green = green
        self._blue = blue
        self._alpha = alpha
        return self

    ###################################
    #           Calculate
    ###################################
    def __add__(self, other: "RGBAColor") -> "RGBAColor":
        # TODO: ADD ORIGINAL OPACITY
        my_colo = self.get_rgb()
        ot_colo = other.get_rgba()

        # Calc colors
        red = int(my_colo[0]*(1-ot_colo[3]) + ot_colo[3]*ot_colo[0])
        green = int(my_colo[1] * (1 - ot_colo[3]) + ot_colo[3] * ot_colo[1])
        blue = int(my_colo[2] * (1 - ot_colo[3]) + ot_colo[3] * ot_colo[2])

        return RGBAColor(red, green, blue, 1., self.get_bit())


class RGBColor(RGBAColor):
    """
    Represents a rgb color
    """
    def __init__(self, red: int = 0, green: int = 0, blue: int = 0, nbits: int = 8):
        super(RGBColor, self).__init__(red, green, blue, nbits=nbits)


class Colors(enum.Enum):
    WHITE = RGBColor(255, 255, 255)
    BLACK = RGBColor(0, 0, 0)


class ColorProperties:
    TRANSPARENT_COLOR = Colors.WHITE
