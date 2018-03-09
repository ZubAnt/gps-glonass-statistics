import matplotlib as mpl
import matplotlib.pyplot as plt
from models.statistics import Statistics

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 14


class StatisticsPlotter(object):
    def plot(self, s: Statistics):
        plt.figure(1)
        plt.plot(s.power, s.s_x)
        self._set_grid(plt)
        self._set_x_label(plt, r'$\mathdefault{P}_{помехи}$, dBm')
        plt.show()

    def plot_sigma_x_of_gps_only(self, narrow: Statistics, freq_mod: Statistics, psp_mod: Statistics) -> None:
        plt.plot(narrow.power, narrow.s_x, 'r--')
        plt.plot(freq_mod.power, freq_mod.s_x, 'b:')
        plt.plot(psp_mod.power, psp_mod.s_x, 'g-.')

        self._set_grid(plt)
        self._set_x_label(plt, r'$\mathdefault{P}_{помехи}$, dBm')
        plt.show()

    def plot_sigma_y_of_gps_only(self, narrow: Statistics, freq_mod: Statistics, psp_mod: Statistics) -> None:
        plt.plot(narrow.power, narrow.s_y, 'r--')
        plt.plot(freq_mod.power, freq_mod.s_y, 'b:')
        plt.plot(psp_mod.power, psp_mod.s_y, 'g-.')

        self._set_grid(plt)
        self._set_x_label(plt, r'$\mathdefault{P}_{помехи}$, dBm')
        plt.show()

    def plot_sigma_z_of_gps_only(self, narrow: Statistics, freq_mod: Statistics, psp_mod: Statistics) -> None:
        plt.plot(narrow.power, narrow.s_z, 'r--')
        plt.plot(freq_mod.power, freq_mod.s_z, 'b:')
        plt.plot(psp_mod.power, psp_mod.s_z, 'g-.')

        self._set_grid(plt)
        self._set_x_label(plt, r'$\mathdefault{P}_{помехи}$, dBm')
        plt.show()

    @classmethod
    def _set_grid(cls, p: plt) -> plt:
        p.grid(True)

    @classmethod
    def _set_x_label(cls, p: plt, label: str):
        p.xlabel(label, fontsize=18)

    @classmethod
    def _set_y_label(cls, p: plt, label: str):
        p.ylabel(label, fontsize=18)
