from models.statistics import Statistics
from services.base_statistics_service import BaseStatisticsService


class GPSNarrowBandService(BaseStatisticsService):

    def __init__(self) -> None:
        file = r'../screenshots/gps-on-glon-off/statistics.csv'
        super().__init__(file)

    def _scale_power_axis(self, s: Statistics) -> None:
        scaled_power = []
        for p in s.power:
            scaled_power.append(p - 16 - 15)
        s.power = scaled_power
