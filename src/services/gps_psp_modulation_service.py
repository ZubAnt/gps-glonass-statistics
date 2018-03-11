from models.statistics import Statistics
from services.base_statistics_service import BaseStatisticsService


class GPSpspModulationService(BaseStatisticsService):

    def __init__(self) -> None:
        file = r'../screenshots/gps-psp/statistics.csv'
        super().__init__(file)

    def _scale_power_axis(self, s: Statistics) -> None:
        scaled_power = []
        for p in s.power:
            scaled_power.append(p - 15 - 16)
        s.power = scaled_power
