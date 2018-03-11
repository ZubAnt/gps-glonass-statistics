class Window(object):

    def __init__(self, width: int, hight: int) -> None:
        self._width = width
        self._hight = hight

    @property
    def w(self) -> int:
        return self._width

    @property
    def h(self) -> int:
        return self._hight

    @property
    def w_inch(self) -> float:
        return self._pixel_to_inch(self._width)

    @property
    def h_inch(self):
        return self._pixel_to_inch(self._hight)

    @classmethod
    def _pixel_to_inch(cls, pixel) -> float:
        return pixel * 0.010378
