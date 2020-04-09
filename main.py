from PyQt5 import QtWidgets
from mainMenu import Ui_MainWindow
import sys
import numpy as np

import styles
import funcs
import extrafuncs
from fits2 import firstFit
from extensionsFuncs import preparingForFF, printAll, clearAll
from Genetic_Algorithm_3 import Generic_Algorithm


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

        self.ui.genes_number.setText('25')
        self.ui.ind_number.setText('15')
        self.ui.elite.setText('.1')
        self.ui.mutation_probability.setText('.001')
        self.ui.size_multiplier.setText('4')
        self.ui.xBorder.setText('10')
        self.ui.yBorder.setText('10')
        self.ui.zBorder.setText('10')
        self.ui.number_of_generations.setText('10')

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
                print(self.allDict['currentParal'])

                w.removeItem(self.allDict['placedParals'][self.allDict['currentParal']])

                if len(self.allDict['placedParals']) > 1:
                    i, currentJ, z = self.allDict['allTranslations'][self.allDict['placedParals'][-1]]

                    self.allDict['placedParals'][-1].translate(-i, -currentJ, -z)

                self.allDict['placedParals'].pop()
                self.allDict['matrixOfMatrices'].pop()

                self.allDict['matrices'] = [] if len(self.allDict['matrixOfMatrices']) == 0 else \
                    self.allDict['matrixOfMatrices'][-1]

    def stepForwardButton(self):
        # print(self.allDict['currentParal'])
        # if not self.allDict['parals']:
        #     funcs.randGenes(self, self.allDict['k'])
        #     preparingForFF(self, False)
        #     firstFit(self, True)
        # else:
        #     self.allDict['is_show_parals'] = True
        #     firstFit(self, False)
        #     self.allDict['is_show_parals'] = False

        print('Будет доступна в следующей версии')

        pass

    def startButton(self):
        w = self.ui.gl
        for paral in self.allDict['placedParals']:
            w.removeItem(paral)

        clearAll(self)
        self.allDict['parals'] = []

        mainMenu.getAllData(self)

        funcs.randGenes(self, self.allDict['k'])
        preparingForFF(self, False)
        ga = Generic_Algorithm(self.allDict, self.allParals, number_of_generations=self.number_of_generations,
                               ind_number=self.ind_number, elite=self.elite,
                               mutation_probability=self.mutation_probability)
        ga_best_value, ga_best_solution, _ = ga.main()

        self.allDict['parals'] = ga_best_solution
        self.allDict['is_show_parals'] = True
        preparingForFF(self, False)
        clearAll(self)
        firstFit(self, False)
        self.allDict['is_show_parals'] = False

        self.ui.best_value.setText(str(ga_best_value * 100)[:2] + '%')
        print('Готово!')

    def getAllData(self):
        self.genes_number = int(self.ui.genes_number.text())
        self.ind_number = int(self.ui.ind_number.text())
        self.elite = float(self.ui.elite.text())
        self.mutation_probability = float(self.ui.mutation_probability.text())
        self.size_multiplier = self.allDict['k'] = int(self.ui.size_multiplier.text())
        self.allDict['xBorder'] = int(self.ui.xBorder.text()) + 1
        self.allDict['yBorder'] = int(self.ui.yBorder.text()) + 1
        self.allDict['zBorder'] = int(self.ui.zBorder.text())
        self.number_of_generations = int(self.ui.number_of_generations.text())

        self.allDict['maxSpace'] = self.allDict['xBorder'] * self.allDict['yBorder'] * self.allDict['zBorder']


if __name__ == '__main__':
    allDict = {
        'k': 4,
        'xl': 0, 'yw': 0, 'zh': 0,
        'xBorder': 8,
        'yBorder': 8,
        'zBorder': 8,
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

        'is_show_parals': False,
        'best_individual': [],
        'best_value': .0

    }

    allParals = {}

    app = QtWidgets.QApplication([])
    application = mainMenu(allDict, allParals)
    application.show()

    sys.exit(app.exec())
