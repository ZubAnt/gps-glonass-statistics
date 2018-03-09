class Snapshot(object):

    def __init__(self, power: float,
                 h_dop: float, v_dop: float, t_dop: float,
                 m_lat: float, m_long: float, m_height: float,
                 m_x: float, m_y: float, m_z: float,
                 s_lat: float, s_long: float, s_height: float,
                 s_x: float, s_y: float, s_z: float) -> None:
        self._power = power
        self._h_dop = h_dop
        self._v_dop = v_dop
        self._t_dop = t_dop
        self._m_lat = m_lat
        self._m_long = m_long
        self._m_height = m_height
        self._m_x = m_x
        self._m_y = m_y
        self._m_z = m_z
        self._s_lat = s_lat
        self._s_long = s_long
        self._s_height = s_height
        self._s_x = s_x
        self._s_y = s_y
        self._s_z = s_z

    @property
    def power(self) -> float:
        return self._power

    @property
    def h_dop(self) -> float:
        return self._h_dop

    @property
    def v_dop(self) -> float:
        return self._v_dop

    @property
    def t_dop(self) -> float:
        return self._t_dop

    @property
    def m_lat(self) -> float:
        return self._m_lat

    @property
    def m_long(self) -> float:
        return self._m_long

    @property
    def m_height(self) -> float:
        return self._m_height

    @property
    def m_x(self) -> float:
        return self._m_x

    @property
    def m_y(self) -> float:
        return self._m_y

    @property
    def m_z(self) -> float:
        return self._m_z

    @property
    def s_lat(self) -> float:
        return self._s_lat

    @property
    def s_long(self) -> float:
        return self._s_long

    @property
    def s_height(self) -> float:
        return self._s_height

    @property
    def s_x(self) -> float:
        return self._s_x

    @property
    def s_y(self) -> float:
        return self._s_y

    @property
    def s_z(self) -> float:
        return self._s_z

    def __repr__(self):
        print('here')