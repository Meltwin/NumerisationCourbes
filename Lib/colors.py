import enum
import math


def hex_format(sub_str: str) -> str:
    # TODO: support nbits
    if len(sub_str) == 1:
        return "0"+sub_str
    return sub_str


class Color:
    """
    Factory for colors
    """
    @staticmethod
    def from_hex(hex_string: str) -> "RGBColor":
        """
        Create a RGBColor instance from an hex string
        :param hex_string: #RRGGBB
        :return: a RGBColor instance corresponding to the given hex code
        """
        assert len(hex_string) == 7
        return RGBColor(Color._hex(hex_string[1:3]), Color._hex(hex_string[3:5]), Color._hex(hex_string[5:]))

    @staticmethod
    def _hex(hex_value: str) -> int:
        length = len(hex_value)-1
        power = 0
        num = 0
        while power <= length:
            num += int(hex_value[length-power], 16)*(16**power)
            power += 1
        return num

    @staticmethod
    def red2int(color: float, nb_bits: int = 8) -> int:
        return math.floor(math.floor(color*(2**nb_bits-1)))


class BaseColor:
    """
    Base class for every color
    """
    pass


class RGBColor(BaseColor):
    def __init__(self, red: int, green: int, blue: int, nb_bit: int = 8) -> None:
        super(RGBColor, self).__init__()
        self._red = red
        self._blue = blue
        self._green = green
        self._nb_bits = nb_bit

    def get_red(self) -> int: return self._red
    def get_green(self) -> int: return self._green
    def get_blue(self) -> int: return self._blue
    def get_nb_bits(self) -> int: return self._nb_bits

    def __add__(self, c: "RGBColor" or "RGBAColor") -> "RGBColor":
        # TODO: Adapt color bits
        if type(c) is RGBColor:
            return RGBColor(self._red+c.get_red(), self._green+c.get_green(), self._blue+c.get_blue(), self._nb_bits)
        elif type(c) is RGBAColor:
            a = c.get_alpha
            red = self._red*(1-a) + c.get_red()*a
            green = self._green*(1-a) + c.get_green()*a
            blue = self._blue*(1-a) + c.get_blue()*a
            return RGBColor(red, green, blue, self._nb_bits)

    def __str__(self) -> str:
        """
        Return the hex code for the color
        """
        return f"#{hex_format(hex(self._red)[2:])}{hex_format(hex(self._green)[2:])}{hex_format(hex(self._blue)[2:])}"


class RGBAColor(RGBColor):
    """
    Represents a rgba color
    """
    def __init__(self, red: int = 0, green: int = 0, blue: int = 0, alpha: float = 1., nbits: int = 8):
        super(RGBAColor, self).__init__(red, green, blue, nbits)
        self._alpha = alpha

    def get_alpha(self) -> float:
        return self._alpha
    # TODO: ADDING RGBA + RGBA


class BiColor(BaseColor):
    """
    Two colors : white & black
        - white = True
        - black = False
    """
    def __init__(self, colored: bool):
        super(BiColor, self).__init__()
        self.colored = colored

    def is_colored(self) -> bool: return self.colored


class Colors:
    WHITE = RGBColor(255, 255, 255, nb_bit=8)
    BLACK = RGBColor(0, 0, 0, nb_bit=8)
    TRANSPARENT_COLOR = WHITE
