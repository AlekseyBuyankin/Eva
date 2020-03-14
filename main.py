from PyQt5 import QtCore, QtGui, QtWidgets
from mainMenu import Ui_MainWindow
import sys
import numpy as np

import styles
import funcs
import extrafuncs
import fits


class movenment(QtWidgets.QMainWindow):
    def __init__(self):
        pass

    def center(self):
        desktop = QtWidgets.QDesktopWidget()
        rect = desktop.availableGeometry(desktop.primaryScreen())  # прямоугольник с размерами экрана
        center = rect.center()
        center.setX(center.x() - (self.width() / 2))
        center.setY(center.y() - (self.height() / 2))
        self.move(center)

    def right(self):
        desktop = QtWidgets.QDesktopWidget()
        rect = desktop.availableGeometry(desktop.primaryScreen())  # прямоугольник с размерами экрана
        right = rect.center()
        right.setX(right.x() - (self.width() / 2) + ((self.width() * 3) / 2) + (self.width() / 3) + (self.width() / 18))
        right.setY(right.y() - (self.height() / 2))
        self.move(right)

    def left(self):
        desktop = QtWidgets.QDesktopWidget()
        rect = desktop.availableGeometry(desktop.primaryScreen())  # прямоугольник с размерами экрана
        right = rect.center()
        right.setX(right.x() - (self.width() / 2) - ((self.width() * 3) / 2) - (self.width() / 3) - (self.width() / 18))
        right.setY(right.y() - (self.height() / 2))
        self.move(right)


class mainMenu(QtWidgets.QMainWindow):
    def __init__(self, allDict, allParals):
        super(mainMenu, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.allDict = allDict
        self.allParals = allParals

        movenment.center(self)
        self.setWindowTitle('Byankin Aleksey')

        styles.setStylesForMainWindow(self)
        funcs.makeSurface(self)
        self.ui.gl.setBackgroundColor('#2b2b2b')

        self.ui.stepBackButton.clicked.connect(self.stepBackButton)
        self.ui.stepForwardButton.clicked.connect(self.stepForwardButton)
        self.ui.startButton.clicked.connect(self.startButton)

        # self.allDict['k'] = 2  # множитель размера параллелепипеда
        # self.allDict['xBorder'] = 10
        # self.allDict['yBorder'] = 10
        # self.allDict['zBorder'] = 10

    # def button1(self):
    #     extradefs.onButtonClick(self, self.allDict['buttons'], self.ui.button1)

    # def startButton(self):
    #     extradefs.onButtonClick(self, self.allDict['otherButtons'], self.ui.startButton)
    #
    #     self.timer = QtCore.QTimer()
    #     self.timer.timeout.connect(self.update)
    #     self.timer.start(100)

    def textButton(self):
        if self.allDict['textBox']:
            extrafuncs.removeText(self)
        else:
            extrafuncs.addAllText(self)

    def stepBackButton(self):
        if self.allDict['parals']:
            print('currentParal =', self.allDict['currentParal'])
            if self.allDict['currentParal'] > 0:
                if self.allDict['currentParal'] != len(self.allDict['placedParals']):
                    self.allDict['currentParal'] = len(self.allDict['placedParals']) - 1
                else:
                    self.allDict['currentParal'] -= 1
                w = self.ui.gl

                print('currentParal =', self.allDict['currentParal'])
                print('placedParals:', len(self.allDict['placedParals']), 'currentParal:', self.allDict['currentParal'],
                      self.allDict['placedParals'])
                w.removeItem(self.allDict['placedParals'][self.allDict['currentParal']])

                if len(self.allDict['placedParals']) > 1:
                    i, currentJ, z = self.allDict['allTranslations'][self.allDict['placedParals'][-1]]

                    self.allDict['placedParals'][-1].translate(-i, -currentJ, -z)

                self.allDict['placedParals'].pop()

                print('placedParals:', len(self.allDict['placedParals']), 'currentParal:', self.allDict['currentParal'],
                      self.allDict['placedParals'])

                self.allDict['matrixOfMatrices'].pop()
                self.allDict['matrixXY'] = np.array([]) if len(self.allDict['matrixOfMatrices']) == 0 else \
                    np.array(self.allDict['matrixOfMatrices'][-1])

                print(self.allDict['matrixXY'], '\n')

                pass

        pass

    def stepForwardButton(self):
        if not self.allDict['parals']:
            funcs.population(self, self.allDict['k'])
            fits.firstFit(self, self.allDict['currentParal'], True)
        else:
            fits.firstFit(self, self.allDict['currentParal'], True)

    def startButton(self):
        if not self.allDict['parals']:
            # funcs.randPopulation(self, self.allDict['k'], 25)
            funcs.population(self, self.allDict['k'])
            fits.firstFit(self, 0, False)
        else:
            fits.firstFit(self, self.allDict['currentParal'], False)

    # def update(self):
    #     w = self.ui.gl
    #     xs = self.allDict['x']  # сколько раз можно нарисовать точки
    #     k = self.allDict['counterForUpdater']  # количество повторений процедуры update (сколько точек было нарисовано)
    #
    #     if k == 0 and self.allDict['dots']:
    #         w.removeItem(self.allDict['dots'][0])
    #         self.allDict['dots'] = []
    #
    #     if not self.allDict['dots']:
    #         m3 = defs.dots(self)
    #
    #         self.allDict['dots'].append(m3)
    #         self.allDict['counterForUpdater'] += 1
    #     else:
    #         print('k =', k, 'len(xs) =', len(xs))
    #
    #         if k < len(xs):
    #             w.removeItem(self.allDict['dots'][0])
    #
    #             m3 = defs.dots(self)
    #
    #             self.allDict['dots'][0] = m3
    #             self.allDict['counterForUpdater'] += 1
    #
    #         else:
    #             self.timer.stop()
    #             self.allDict['counterForUpdater'] = 0


if __name__ == '__main__':
    allDict = {
        'k': 2,
        'xl': 0, 'yw': 0, 'zh': 0,
        'xBorder': 10,
        'yBorder': 10,
        'zBorder': 10,

        'parals': [],
        'currentParal': 0,
        'placedParals': [],

        'matrixXY': np.array([[], []]),
        'matrices': [],

        'matrixOfMatrices': [],
        'isBacked': False,

        'allTranslations': {}

    }

    allParals = {}

    app = QtWidgets.QApplication([])
    application = mainMenu(allDict, allParals)
    application.show()

    sys.exit(app.exec())
