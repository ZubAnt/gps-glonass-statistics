from models.statistics import Statistics
from services.base_statistics_service import BaseStatisticsService


class GPSpspModulationService(BaseStatisticsService):

    def __init__(self) -> None:
        file = r'../screenshots/gps-psp/statistics.csv'
        super().__init__(file)

    def _scale_power_axis(self, s: Statistics) -> None:
        scaled_power = []
        for p in s.power:
            if p >= -10:
                new_power = p - 28 - 16
            else:
                new_power = p - 25 - 16
            scaled_power.append(new_power)
        s.power = scaled_power
