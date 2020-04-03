from PyQt5 import QtWidgets
from mainMenu import Ui_MainWindow
import sys
import numpy as np

import styles
import funcs
import extrafuncs
import fits2
from extensionsFuncs import preparingForFF
from genetic_algorithm import geneticAlgorithm, printAll
from Simulated_Annealing import Simulated_Annealing


class movenment(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def center(self):
        desktop = QtWidgets.QDesktopWidget()
        rect = desktop.availableGeometry(desktop.primaryScreen())  # прямоугольник с размерами экрана
        center = rect.center()
        center.setX(int(center.x() - (self.width() / 2)))
        center.setY(int(center.y() - (self.height() / 2)))
        self.move(center)

    def right(self):
        desktop = QtWidgets.QDesktopWidget()
        rect = desktop.availableGeometry(desktop.primaryScreen())  # прямоугольник с размерами экрана
        right = rect.center()
        right.setX(
            int(right.x() - (self.width() / 2) + ((self.width() * 3) / 2) + (self.width() / 3) + (self.width() / 18)))
        right.setY(int(right.y() - (self.height() / 2)))
        self.move(right)

    def left(self):
        desktop = QtWidgets.QDesktopWidget()
        rect = desktop.availableGeometry(desktop.primaryScreen())  # прямоугольник с размерами экрана
        right = rect.center()
        right.setX(
            int(right.x() - (self.width() / 2) - ((self.width() * 3) / 2) - (self.width() / 3) - (self.width() / 18)))
        right.setY(int(right.y() - (self.height() / 2)))
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

        self.allDict['maxSpace'] = self.allDict['xBorder'] * self.allDict['yBorder'] * self.allDict['zBorder']

        funcs.population(self, self.allDict['k'])
        preparingForFF(self, False)
        # fits2.firstFit(self, False)
        # x, y = geneticAlgorithm(self)

        self.allDict['is_show_parals'] = False


        s_a = Simulated_Annealing(self.allDict, self.allParals)
        s_a.main()

        # self.allDict['k'] = 2  # множитель размера параллелепипеда
        # self.allDict['xBorder'] = 10
        # self.allDict['yBorder'] = 10
        # self.allDict['zBorder'] = 10

    def textButton(self):
        if self.allDict['textBox']:
            extrafuncs.removeText(self)
        else:
            extrafuncs.addAllText(self)

    def stepBackButton(self):
        if self.allDict['parals']:  # если объекты есть на плоскости
            if self.allDict['currentParal'] > 0:
                if self.allDict['currentParal'] != len(self.allDict['placedParals']):
                    self.allDict['currentParal'] = len(self.allDict['placedParals']) - 1
                else:
                    self.allDict['currentParal'] -= 1
                w = self.ui.gl

                w.removeItem(self.allDict['placedParals'][self.allDict['currentParal']])

                if len(self.allDict['placedParals']) > 1:
                    i, currentJ, z = self.allDict['allTranslations'][self.allDict['placedParals'][-1]]

                    self.allDict['placedParals'][-1].translate(-i, -currentJ, -z)

                self.allDict['placedParals'].pop()
                self.allDict['matrixOfMatrices'].pop()

                self.allDict['matrices'] = [] if len(self.allDict['matrixOfMatrices']) == 0 else \
                    self.allDict['matrixOfMatrices'][-1]

    def stepForwardButton(self):
        if not self.allDict['parals']:
            funcs.population(self, self.allDict['k'])
            preparingForFF(self, False)
            fits2.firstFitDecreasing(self, True)
        else:
            fits2.firstFitDecreasing(self, True)

    def startButton(self):
        if not self.allDict['parals']:
            # funcs.randPopulation(self, self.allDict['k'], 25)
            funcs.population(self, self.allDict['k'])
            preparingForFF(self, False)
            fits2.firstFitDecreasing(self, False)
        else:
            fits2.firstFitDecreasing(self, False)


if __name__ == '__main__':
    allDict = {
        'k': 2,
        'xl': 0, 'yw': 0, 'zh': 0,
        'xBorder': 7,
        'yBorder': 7,
        'zBorder': 7,
        'maxSpace': 0,

        'parals': [],
        'paral_dict': [],
        'currentParal': 0,
        'placedParals': [],

        'matrixXY': np.array([[], []]),
        'matrices': [],

        'matrixOfMatrices': [],
        'isBacked': False,

        'allTranslations': {},

        'number_of_iteration': 300,
        'ind_number': 0,
        'crossed_number': 0,
        'selected_number': 0,
        'mutation_probability': 0,
        'is_show_parals': True,
        'best_individual': [],
        'best_value': .0

    }

    allParals = {}

    app = QtWidgets.QApplication([])
    application = mainMenu(allDict, allParals)
    # application.show()

    sys.exit(app.exec())
