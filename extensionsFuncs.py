import numpy as np


def createMatrices(self):
    for _ in range(self.allDict['zBorder']):
        createMatrix(self)
        self.allDict['matrices'].append(self.allDict['matrixXY'])


def createMatrix(self):
    self.allDict['matrixXY'] = np.zeros((self.allDict['xBorder'],
                                         self.allDict['yBorder']))


def isAvailableY(self, rowIndex, colIndex, paralX, paralY):
    for x in range(colIndex, colIndex + paralX):
        for y in range():
            pass



    pass


# проверить свободное место в верхних слоях
def isAvailableZ(self, savedZ, paralZ, fromI, toI, fromJ, toJ):
    matrices = self.allDict['matrices'][savedZ + 1: savedZ + 1 + paralZ]

    # print('Поиск в верхних слоях:')
    # writeToAllMatrices(self, savedZ + 1, paralZ, fromI, toI, fromJ, toJ)

    for numMatrix in range(len(matrices)):
        matrixXY = self.allDict['matrixXY']
        for x in range(fromI, toI):
            for y in range(fromJ, toJ):
                if matrixXY[x, y] == 1:
                    return False

    return True


# записать данные об объекте в матрицы всех занимаемых им слоев
def writeToAllMatrices(self, savedZ, paralZ, fromI, toI, fromJ, toJ):
    matrices = self.allDict['matrices'][savedZ: savedZ + paralZ]

    for numMatrix in range(len(matrices)):
        for x in range(fromI, toI):
            for y in range(fromJ, toJ):
                self.allDict['matrixXY'][x, y] = 1
        self.allDict['matrices'][numMatrix] = self.allDict['matrixXY']


def printMatricesToString(self, savedZ, paralZ):
    s = ''

    matrices = self.allDict['matrices'][savedZ: savedZ + paralZ]

    for row in range(len(matrices[0])):
        for numMatrix in range(len(matrices)):
            s += str(matrices[numMatrix][row]) + '  '
        s += '\n'

    print(s)


def writeFirstParal(self):
    paral = self.allDict['parals'][0]
    (_, _, paralZ) = self.allParals[paral]

    writeToAllMatrices(self, 0, paralZ, 0, 0, 0, 0)
