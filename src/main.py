from models.statistics import Statistics
from plotters.statistics_plotter import StatisticsPlotter
from services.gps_frequence_modulation_service import GPSFrequenceModulationService
from services.gps_narrow_band_service import GPSNarrowBandService
from services.gps_psp_modulation_service import GPSpspModulationService


def main():
    plotter = StatisticsPlotter()

    gps_narrow_band_stat = GPSNarrowBandService().get_statistics()
    gps_freq_mod_stat = GPSFrequenceModulationService().get_statistics()
    gps_psp_mod_stat = GPSpspModulationService().get_statistics()

    plotter.plot_sigma_x_of_gps_only(gps_narrow_band_stat, gps_freq_mod_stat, gps_psp_mod_stat)
    plotter.plot_sigma_y_of_gps_only(gps_narrow_band_stat, gps_freq_mod_stat, gps_psp_mod_stat)
    plotter.plot_sigma_z_of_gps_only(gps_narrow_band_stat, gps_freq_mod_stat, gps_psp_mod_stat)

    # plotter.plot(gps_psp_mod_stat)


if __name__ == "__main__":
    main()

