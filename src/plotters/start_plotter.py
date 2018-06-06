from random import random, randint
import pylab as P

import numpy as np
from time import sleep

import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.pyplot import close
from models.statistics import Statistics
from models.window import Window

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 30


class StartPlotter(object):

    def __init__(self):
        self._saved_path = r'../graphics/gateway/start'
        self._manager = plt.get_current_fig_manager()
        self._window = Window(*self._manager.window.maxsize())

        self._full_screen_enable()

    def plot(self):
        plt.figure(1)
        x = np.arange(8)
        self._set_grid(plt)
        self._set_y_label(plt, r'$\mathdefault{t}_{хол}$, c')
        plt.bar(x, height=[26, 34, 34, 40, 32, 38, 40, 55], capsize=10)
        plt.xticks(x + 0.0, ['GPS',
                            'GPS + УП',
                            'GPS + ЧМ',
                            'GPS + ФКМ',
                            'ГЛОНАСС',
                            'ГЛОНАСС + УП',
                            'ГЛОНАСС + ЧМ',
                            'ГЛОНАСС + ФКМ'], rotation='45')
        plt.subplots_adjust(bottom=0.3)
        self._save("cool_start.png")
        # plt.show()
        close('all')

    def plot_js(self):
        plt.figure(1)
        x = np.arange(6)
        self._set_grid(plt)
        self._set_y_label(plt, r'$\mathdefault{t}_{хол}$, c')
        plt.bar(x, height=[35, 30, 24, 40, 35, 27], capsize=10)
        plt.xticks(x + 0.0, ['GPS + УП',
                            'GPS + ЧМ',
                            'GPS + ФКМ',
                            'ГЛОНАСС + УП',
                            'ГЛОНАСС + ЧМ',
                            'ГЛОНАСС + ФКМ'], rotation='45')
        plt.subplots_adjust(bottom=0.3)
        self._save("js.png")
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

    def _save_glonass(self, filename: str) -> None:
        fig = matplotlib.pyplot.gcf()
        fig.set_size_inches(self._window.w_inch, self._window.h_inch, forward=False)
        fig.savefig(rf"{self._saved_path_glonass}/{filename}", format='png')

    def _full_screen_enable(self) -> None:
        self._manager.resize(*self._manager.window.maxsize())
        # self._manager.full_screen_toggle()