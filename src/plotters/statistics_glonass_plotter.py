from time import sleep

import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.pyplot import close
from models.statistics import Statistics
from models.window import Window

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 30


class StatisticsGlonassPlotter(object):

    def __init__(self):
        self._saved_path = r'../graphics/gateway/glonass'
        self._manager = plt.get_current_fig_manager()
        self._window = Window(*self._manager.window.maxsize())

        self._full_screen_enable()

    def plot(self, s: Statistics):
        plt.figure(1)
        plt.plot(s.power, s.s_x)
        self._set_grid(plt)
        self._set_x_label(plt, r'$\mathdefault{P}_{помехи}$, dBm')
        # plt.show()
        close('all')

    def plot_sigma_x_of_glonass_only(self, narrow: Statistics, freq_mod: Statistics, psp_mod: Statistics) -> None:
        plt.plot(narrow.power, narrow.s_x, 'r-', label="узкополосная помеха", linewidth=3, marker='o', markersize=9)
        plt.plot(freq_mod.power, freq_mod.s_x, 'b-.', label="чм помеха", linewidth=3, marker='s', markersize=9)
        plt.plot(psp_mod.power, psp_mod.s_x, 'g--', label="фкм помеха (ПСП)", linewidth=3, marker='^', markersize=9)

        self._set_grid(plt)
        self._set_x_label(plt, r'$\mathdefault{P}_{помехи}$, dBm')
        self._set_y_label(plt, r'$\sigma_x, м^{2}$')
#         # plt.title("Зависимость СКО координаты X от уровня мощности помехи в тракте")
        plt.legend()

        self._save("glonass_only_sigma_x.png")

        # plt.show()
        close('all')

    def plot_sigma_y_of_glonass_only(self, narrow: Statistics, freq_mod: Statistics, psp_mod: Statistics) -> None:
        plt.plot(narrow.power, narrow.s_y, 'r-', label="узкополосная помеха", linewidth=3, marker='o', markersize=9)
        plt.plot(freq_mod.power, freq_mod.s_y, 'b-.', label="чм помеха", linewidth=3, marker='s', markersize=9)
        plt.plot(psp_mod.power, psp_mod.s_y, 'g--', label="фкм помеха (ПСП)", linewidth=3, marker='^', markersize=9)

        self._set_grid(plt)
        self._set_x_label(plt, r'$\mathdefault{P}_{помехи}$, dBm')
        self._set_y_label(plt, r'$\sigma_y, м^{2}$')
        # plt.title("Зависимость СКО координаты Y от уровня мощности помехи в тракте")
        plt.legend()

        self._save("glonass_only_sigma_y.png")

        # plt.show()
        close('all')

    def plot_sigma_z_of_glonass_only(self, narrow: Statistics, freq_mod: Statistics, psp_mod: Statistics) -> None:
        plt.plot(narrow.power, narrow.s_z, 'r-', label="узкополосная помеха", linewidth=3, marker='o', markersize=9)
        plt.plot(freq_mod.power, freq_mod.s_z, 'b-.', label="чм помеха", linewidth=3, marker='s', markersize=9)
        plt.plot(psp_mod.power, psp_mod.s_z, 'g--', label="фкм помеха (ПСП)", linewidth=3, marker='^', markersize=9)

        self._set_grid(plt)
        self._set_x_label(plt, r'$\mathdefault{P}_{помехи}$, dBm')
        self._set_y_label(plt, r'$\sigma_z, м^{2}$')
        # plt.title("Зависимость СКО координаты Z от уровня мощности помехи в тракте")
        plt.legend()

        self._save("glonass_only_sigma_z.png")

        # plt.show()
        close('all')

    def plot_sigma_lat_of_glonass_only(self, narrow: Statistics, freq_mod: Statistics, psp_mod: Statistics) -> None:
        plt.plot(narrow.power, narrow.s_lat, 'r-', label="узкополосная помеха", linewidth=3, marker='o', markersize=9)
        plt.plot(freq_mod.power, freq_mod.s_lat, 'b-.', label="чм помеха", linewidth=3, marker='s', markersize=9)
        plt.plot(psp_mod.power, psp_mod.s_lat, 'g--', label="фкм помеха (ПСП)", linewidth=3, marker='^', markersize=9)

        self._set_grid(plt)
        self._set_x_label(plt, r'$\mathdefault{P}_{помехи}$, dBm')
        self._set_y_label(plt, r'$\sigma_{latitude}, c^{2}$')
        # plt.title("Зависимость СКО широты от уровня мощности помехи в тракте")
        plt.legend()

        self._save("glonass_only_sigma_lat.png")

        # plt.show()
        close('all')

    def plot_sigma_log_of_glonass_only(self, narrow: Statistics, freq_mod: Statistics, psp_mod: Statistics) -> None:
        plt.plot(narrow.power, narrow.s_long, 'r-', label="узкополосная помеха", linewidth=3, marker='o', markersize=9)
        plt.plot(freq_mod.power, freq_mod.s_long, 'b-.', label="чм помеха", linewidth=3, marker='s', markersize=9)
        plt.plot(psp_mod.power, psp_mod.s_long, 'g--', label="фкм помеха (ПСП)", linewidth=3, marker='^', markersize=9)

        self._set_grid(plt)
        self._set_x_label(plt, r'$\mathdefault{P}_{помехи}$, dBm')
        self._set_y_label(plt, r'$\sigma_{longitude}, c^{2}$')
        # plt.title("Зависимость СКО долготы от уровня мощности помехи в тракте")
        plt.legend()

        self._save("glonass_only_sigma_long.png")

        # plt.show()
        close('all')

    def plot_math_exp_x_of_glonass_only(self, narrow: Statistics, freq_mod: Statistics, psp_mod: Statistics) -> None:
        plt.plot(narrow.power, narrow.m_x, 'r-', label="узкополосная помеха", linewidth=3, marker='o', markersize=9)
        plt.plot(freq_mod.power, freq_mod.m_x, 'b-.', label="чм помеха", linewidth=3, marker='s', markersize=9)
        plt.plot(psp_mod.power, psp_mod.m_x, 'g--', label="фкм помеха (ПСП)", linewidth=3, marker='^', markersize=9)

        self._set_grid(plt)
        self._set_x_label(plt, r'$\mathdefault{P}_{помехи}$, dBm')
        self._set_y_label(plt, r'$\mathdefault{m}_{x}$, м')
        # plt.title("Зависимость мат. ожидания координаты X от уровня мощности помехи в тракте")
        plt.legend()

        self._save("glonass_only_math_exp_x.png")

        # plt.show()
        close('all')

    def plot_math_exp_y_of_glonass_only(self, narrow: Statistics, freq_mod: Statistics, psp_mod: Statistics) -> None:
        plt.plot(narrow.power, narrow.m_y, 'r-', label="узкополосная помеха", linewidth=3, marker='o', markersize=9)
        plt.plot(freq_mod.power, freq_mod.m_y, 'b-.', label="чм помеха", linewidth=3, marker='s', markersize=9)
        plt.plot(psp_mod.power, psp_mod.m_y, 'g--', label="фкм помеха (ПСП)", linewidth=3, marker='^', markersize=9)

        self._set_grid(plt)
        self._set_x_label(plt, r'$\mathdefault{P}_{помехи}$, dBm')
        self._set_y_label(plt, r'$\mathdefault{m}_{y}$, м')
        # plt.title("Зависимость мат. ожидания координаты Y от уровня мощности помехи в тракте")
        plt.legend()

        self._save("glonass_only_math_exp_y.png")

        # plt.show()
        close('all')

    def plot_math_exp_z_of_glonass_only(self, narrow: Statistics, freq_mod: Statistics, psp_mod: Statistics) -> None:
        plt.plot(narrow.power, narrow.m_z, 'r-', label="узкополосная помеха", linewidth=3, marker='o', markersize=9)
        plt.plot(freq_mod.power, freq_mod.m_z, 'b-.', label="чм помеха", linewidth=3, marker='s', markersize=9)
        plt.plot(psp_mod.power, psp_mod.m_z, 'g--', label="фкм помеха (ПСП)", linewidth=3, marker='^', markersize=9)

        self._set_grid(plt)
        self._set_x_label(plt, r'$\mathdefault{P}_{помехи}$, dBm')
        self._set_y_label(plt, r'$\mathdefault{m}_{z}$, м')
        # plt.title("Зависимость мат. ожидания координаты Z от уровня мощности помехи в тракте")
        plt.legend()

        self._save("glonass_only_math_exp_z.png")

        # plt.show()
        close('all')

    def plot_math_exp_lat_of_glonass_only(self, narrow: Statistics, freq_mod: Statistics, psp_mod: Statistics) -> None:
        plt.plot(narrow.power, narrow.m_lat, 'r-', label="узкополосная помеха", linewidth=3, marker='o', markersize=9)
        plt.plot(freq_mod.power, freq_mod.m_lat, 'b-.', label="чм помеха", linewidth=3, marker='s', markersize=9)
        plt.plot(psp_mod.power, psp_mod.m_lat, 'g--', label="фкм помеха (ПСП)", linewidth=3, marker='^', markersize=9)

        self._set_grid(plt)
        self._set_x_label(plt, r'$\mathdefault{P}_{помехи}$, dBm')
        self._set_y_label(plt, r'$\mathdefault{m}_{latitude}$, c')
        # plt.title("Зависимость мат. ожидания широты от уровня мощности помехи в тракте")
        plt.legend()

        self._save("glonass_only_math_exp_lat.png")

        # plt.show()
        close('all')

    def plot_math_exp_long_of_glonass_only(self, narrow: Statistics, freq_mod: Statistics, psp_mod: Statistics) -> None:
        plt.plot(narrow.power, narrow.m_long, 'r-', label="узкополосная помеха", linewidth=3, marker='o', markersize=9)
        plt.plot(freq_mod.power, freq_mod.m_long, 'b-.', label="чм помеха", linewidth=3, marker='s', markersize=9)
        plt.plot(psp_mod.power, psp_mod.m_long, 'g--', label="фкм помеха (ПСП)", linewidth=3, marker='^', markersize=9)

        self._set_grid(plt)
        self._set_x_label(plt, r'$\mathdefault{P}_{помехи}$, dBm')
        self._set_y_label(plt, r'$\mathdefault{m}_{longitude}$, c')
        # plt.title("Зависимость мат. ожидания долготы от уровня мощности помехи в тракте")
        plt.legend()

        self._save("glonass_only_math_exp_long.png")

        # plt.show()
        close('all')

    @classmethod
    def _set_grid(cls, p: plt) -> plt:
        p.grid(True)

    @classmethod
    def _set_x_label(cls, p: plt, label: str):
        p.xlabel(label, fontsize=36)

    @classmethod
    def _set_y_label(cls, p: plt, label: str):
        p.ylabel(label, fontsize=36)

    def _save(self, filename: str) -> None:
        fig = matplotlib.pyplot.gcf()
        fig.set_size_inches(self._window.w_inch, self._window.h_inch, forward=False)
        fig.savefig(rf"{self._saved_path}/{filename}", format='png')

    def _full_screen_enable(self) -> None:
        self._manager.resize(*self._manager.window.maxsize())
        # self._manager.full_screen_toggle()