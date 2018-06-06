import random
from typing import List


class Statistics(object):

    def __init__(self, power: List[float],
                 h_dop: List[float], v_dop: List[float], t_dop: List[float],
                 m_lat: List[float], m_long: List[float], m_height: List[float],
                 m_x: List[float], m_y: List[float], m_z: List[float],
                 s_lat: List[float], s_long: List[float], s_height: List[float],
                 s_x: List[float], s_y: List[float], s_z: List[float]) -> None:
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
    def power(self) -> List[float]:
        return self._power

    @property
    def h_dop(self) -> List[float]:
        return self._h_dop

    @property
    def v_dop(self) -> List[float]:
        return self._v_dop

    @property
    def t_dop(self) -> List[float]:
        return self._t_dop

    @property
    def m_lat(self) -> List[float]:
        return self._m_lat

    @property
    def m_long(self) -> List[float]:
        return self._m_long

    @property
    def m_height(self) -> List[float]:
        return self._m_height

    @property
    def m_x(self) -> List[float]:
        return self._m_x

    @property
    def m_y(self) -> List[float]:
        return self._m_y

    @property
    def m_z(self) -> List[float]:
        return self._m_z

    @property
    def s_lat(self) -> List[float]:
        return self._s_lat

    @property
    def s_long(self) -> List[float]:
        return self._s_long

    @property
    def s_height(self) -> List[float]:
        return self._s_height

    @property
    def s_x(self) -> List[float]:
        return self._s_x

    @property
    def s_y(self) -> List[float]:
        return self._s_y

    @property
    def s_z(self) -> List[float]:
        return self._s_z

    @power.setter
    def power(self, value):
        self._power = value

    def add_random(self):
        for idx in range(1, len(self.power)):
            self._m_lat[idx] = self._get_random(self._m_lat[idx - 1], self._m_lat[idx])
            self._m_long[idx] = self._get_random(self._m_long[idx - 1], self._m_long[idx])
            self._m_height[idx] = self._get_random(self._m_height[idx - 1], self._m_height[idx])
            self._m_x[idx] = self._get_random(self._m_x[idx - 1], self._m_x[idx])
            self._m_y[idx] = self._get_random(self._m_y[idx - 1], self._m_y[idx])
            self._m_z[idx] = self._get_random(self._m_z[idx - 1], self._m_z[idx])
            self._s_lat[idx] = self._get_random(self._s_lat[idx - 1], self._s_lat[idx])
            self._s_long[idx] = self._get_random(self._s_long[idx - 1], self._s_long[idx])
            self._s_height[idx] = self._get_random(self._s_height[idx - 1], self._s_height[idx])
            self._s_x[idx] = self._get_random(self._s_x[idx - 1], self._s_x[idx])
            self._s_y[idx] = self._get_random(self._s_y[idx - 1], self._s_y[idx])
            self._s_z[idx] = self._get_random(self._s_z[idx - 1], self._s_z[idx])

    @staticmethod
    def _get_random(prev_val: float, next_val: float) -> float:
        delta = next_val - prev_val

        if abs(delta) <= 0.0001:
            add_delta = random.uniform(-0.0001, 0.0001)
        elif abs(delta) <= 0.001:
            add_delta = random.uniform(-0.001, 0.001)
        elif abs(delta) <= 0.01:
            add_delta = random.uniform(-0.01, 0.01)
        elif abs(delta) <= 0.1:
            add_delta = random.uniform(-0.05, 0.05)
        elif abs(delta) <= 1:
            add_delta = random.uniform(-0.2, 0.2)
        elif abs(delta) <= 1.5:
            add_delta = random.uniform(-0.5, 0.5)
        elif abs(delta) <= 2:
            add_delta = random.uniform(-0.8, 0.8)
        elif abs(delta) <= 3:
            add_delta = random.uniform(-1, 1)
        elif abs(delta) <= 3.5:
            add_delta = random.uniform(-1.5, 1.5)
        elif abs(delta) <= 4:
            add_delta = random.uniform(-2, 2)
        else:
            add_delta = random.uniform(-3, 3)

        if next_val + add_delta < 0:
            delta_zero = abs(next_val)
            rand_delta_zero = random.uniform(0.0, delta_zero)
            return rand_delta_zero

        return next_val + add_delta
