from models.statistics import Statistics
from services.base_statistics_service import BaseStatisticsService


class GlonassFrequenceModulationService(BaseStatisticsService):

    def __init__(self) -> None:
        file = r'../screenshots/glonass/only-glonass-fm-dev-1.023MHz-rate-1kHz/statistics_fm.csv'
        super().__init__(file)

    def get_statistics(self) -> Statistics:
        s = super().get_statistics()
        # s.add_random()
        return s

    def _scale_power_axis(self, s: Statistics) -> None:
        scaled_power = []
        for p in s.power:
            scaled_power.append(p - 16 - 15)
        s.power = scaled_power
