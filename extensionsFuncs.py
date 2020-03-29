import numpy as np


def createMatrices(self):
    for _ in range(self.allDict['zBorder']):
        createMatrix(self)
        self.allDict['matrices'].append(self.allDict['matrixXY'])


def createMatrix(self):
    self.allDict['matrixXY'] = np.zeros((self.allDict['xBorder'],
                                         self.allDict['yBorder']))


# проверить свободное место только в нижнем слое
def isAvailableY(self, rowIndex, colIndex, paralX, paralY):
    matrixXY = self.allDict['matrices'][0]

    for x in range(rowIndex, rowIndex + paralX + 1):
        for y in range(colIndex, colIndex + paralY + 1):
            if matrixXY[x, y] == 1:
                return False

    return True


# проверить свободное место во всех слоях
def isAvailableXYZ(self, rowIndex, colIndex, beginZ):
    currentParal = self.allDict['currentParal']
    paral = self.allDict['parals'][currentParal]
    (paralX, paralY, paralZ) = self.allParals[paral]
    matrices = self.allDict['matrices'][beginZ: beginZ + paralZ]

    print('Проверяем свободное место по X, Y, Z')
    print('rowIndex:', rowIndex, 'paralX:', paralX, 'colIndex:', colIndex, 'paralY:', paralY)
    print()
    print(matrices)
    print()

    for matrixXY in matrices:
        for x in range(rowIndex, rowIndex + paralX):
            for y in range(colIndex, colIndex + paralY):
                if matrixXY[x, y] != 0:
                    print('Место занято в ячейке', x, y, print(matrixXY[x, y]))
                    return False
    print('Место свободно')
    return True


# записать данные об объекте в матрицы всех занимаемых им слоев
def writeToAllMatrices(self, rowIndex, colIndex, beginZ):
    currentParal = self.allDict['currentParal']
    paral = self.allDict['parals'][currentParal]
    (paralX, paralY, paralZ) = self.allParals[paral]

    matrices = np.array(self.allDict['matrices'][beginZ: beginZ + paralZ])

    for numMatrix in range(len(matrices)):
        matrixXY = np.array(matrices[numMatrix])

        for x in range(rowIndex, rowIndex + paralX):
            for y in range(colIndex, colIndex + paralY):
                matrixXY[x, y] = currentParal + 1
        self.allDict['matrices'][beginZ + numMatrix] = np.array(matrixXY)
        self.allDict['matrixXY'] = np.array(matrixXY)


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

