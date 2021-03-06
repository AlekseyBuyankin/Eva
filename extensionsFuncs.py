import numpy as np
from numba import njit


def createMatrices(self):
    for _ in range(self.allDict['zBorder']):
        createMatrix(self)
        self.allDict['matrices'].append(self.allDict['matrixXY'])


def createMatrix(self):
    self.allDict['matrixXY'] = np.zeros((self.allDict['xBorder'],
                                         self.allDict['yBorder']))


def writeToAllMatrices(self, row_index, col_index, beginZ):
    current_paral = self.allDict['currentParal']
    paral = self.allDict['parals'][current_paral]
    (paralX, paralY, paralZ) = self.allParals[paral]

    matrices = np.array(self.allDict['matrices'][beginZ: beginZ + paralZ])

    for numMatrix in range(len(matrices)):
        matrixXY = np.array(matrices[numMatrix])

        for x in range(row_index, row_index + paralX):
            for y in range(col_index, col_index + paralY):
                matrixXY[x, y] = current_paral + 1
        self.allDict['matrices'][beginZ + numMatrix] = np.array(matrixXY)
        self.allDict['matrixXY'] = np.array(matrixXY)


# проверить свободное место во всех слоях
def isAvailableXYZ(self, row_index, col_index, beginZ):
    current_paral = int(self.allDict['currentParal'])
    paral = self.allDict['parals'][current_paral]
    (paralX, paralY, paralZ) = self.allParals[paral]
    matrices = self.allDict['matrices'][beginZ: beginZ + paralZ]
    for matrixXY in matrices:
        for x in range(row_index, row_index + paralX):
            for y in range(col_index, col_index + paralY):
                if matrixXY[x, y] != 0 and matrixXY[x, y] is not None:
                    # print('Место занято в ячейке', x, y, print(matrixXY[x, y]))
                    return False
    # print('Место свободно')
    return True


# записать данные об объекте в матрицы всех занимаемых им слоев
def printAllMatrices(self):
    printMatricesToString(self, 0, len(self.allDict['matrices']))
    print()


def printMatricesToString(self, beginZ, paralZ):
    s = ''

    matrices = self.allDict['matrices'][beginZ: beginZ + paralZ]

    if len(matrices) > 0:
        for row in range(len(matrices[0])):
            for numMatrix in range(len(matrices)):
                s += str(matrices[numMatrix][row]) + '  '
            if row != len(matrices[0]) - 1:
                s += '\n'

        print(s)


def printMatrix(matrixXY: np.array):
    print('Матрица XY:')
    for row in matrixXY:
        print(row)

    print()


def preparingForFF(self, isDecreasing):
    paral_dict = list([(paral, self.allParals[paral][0], self.allParals[paral][1], self.allParals[paral][2],
                        self.allParals[paral][0] * self.allParals[paral][1] * self.allParals[paral][2]) for paral in
                       self.allDict['parals']])

    if isDecreasing:
        paral_dict = list(sorted(paral_dict, key=lambda k: k[4], reverse=True))
    self.allDict['parals'] = list([paral[0] for paral in paral_dict])
    self.allDict['paral_dict'] = list(paral_dict)


def printAll(obj):
    print('\n'.join(str(e) for e in obj))
    print()


def clearAll(self):
    self.allDict['placedParals'] = list()
    self.allDict['matrices'] = list()
    self.allDict['matrixOfMatrices'] = list()
    self.allDict['currentParal'] = 0
    self.allDict['allTranslations'] = dict()
