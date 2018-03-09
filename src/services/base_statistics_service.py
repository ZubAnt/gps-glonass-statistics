from abc import abstractmethod

from models.statistics import Statistics
from serializers.statistics_serializer import StatisticsSerializer


class BaseStatisticsService(object):

    def __init__(self, file: str):
        self._file = file

    def get_statistics(self) -> Statistics:
        s = StatisticsSerializer.load(self._file)
        self._scale_power_axis(s)
        return s

    @abstractmethod
    def _scale_power_axis(self, s: Statistics) -> None:
        raise NotImplementedError
