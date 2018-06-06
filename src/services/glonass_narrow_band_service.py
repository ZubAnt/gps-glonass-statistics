from models.statistics import Statistics
from services.base_statistics_service import BaseStatisticsService


class GlonassNarrowBandService(BaseStatisticsService):

    def __init__(self) -> None:
        file = r'../screenshots/glonass/gps-off-glon-on/statistics_up.csv'
        super().__init__(file)

    def get_statistics(self) -> Statistics:
        s = super().get_statistics()
        # s.add_random()
        return s

    def _scale_power_axis(self, s: Statistics) -> None:
        scaled_power = []
        for p in s.power:
            scaled_power.append(p - 15 - 15)
        s.power = scaled_power
