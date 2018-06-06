from models.statistics import Statistics
from services.base_statistics_service import BaseStatisticsService


class GlonasspspModulationService(BaseStatisticsService):

    def __init__(self) -> None:
        file = r'../screenshots/glonass/glonass-psp/statistics_fkm.csv'
        super().__init__(file)

    def get_statistics(self) -> Statistics:
        s = super().get_statistics()
        # s.add_random()
        return s

    def _scale_power_axis(self, s: Statistics) -> None:
        scaled_power = []
        for p in s.power:
            if -10.1 < p < -9.9:
                new_power = -68
            elif -5.1 < p < -4.9:
                new_power = -65
            elif -0.1 < p < 0.1:
                new_power = -60
            elif p >= -10:
                new_power = p - 10 - 30 - 16 - 4
            else:
                new_power = p - 10 - 30 - 16
            scaled_power.append(new_power)
        s.power = scaled_power
