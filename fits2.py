from extensionsFuncs import *


def firstFit(self, currentParal, flag):
    createMatrices(self)

    if currentParal < len(self.allDict['parals']):
        print('currentParal:', currentParal, self.allParals[self.allDict['parals'][currentParal]])
    else:
        print('currentParal:', currentParal)

    recFF(self, currentParal, flag)
    pass


def recFF(self, currentParal, flag):
    # если объект первый
    if currentParal == 0:
        paral = self.allDict['parals'][currentParal]
        (paralX, paralY, paralZ) = self.allParals[paral]
        window = self.ui.gl
        window.addItem(paral)
        writeToAllMatrices(self, 0, paralZ, 0, paralX, 0, paralY)
        self.allDict['matrixOfMatrices'].append(self.allDict['matrices'])
        currentParal += 1
        self.allDict['currentParal'] += currentParal

        printMatricesToString(self, 0, paralZ)

        if not flag:
            recFF(self, currentParal, flag)

    else:
        recFindPlace(self, currentParal, 0)

    pass


def recFindPlace(self, currentParal, beginZ):
    matrices = self.allDict['matrices']
    if beginZ < len(matrices):
        # переменные
        paral = self.allDict['parals'][currentParal]
        (paralX, paralY, paralZ) = self.allParals[paral]
        matrixXY = matrices[beginZ]

        # проверяем легкими проверками на свободное место
        # проверки:
        # по высоте, по количеству оставшегося места в matrixXY, по X

        # < легкие проверки

        # по высоте
        if paralZ > len(matrices) - beginZ:
            print('Проверка по высоте: нет места для объекта:', (paralX, paralY, paralZ))
            return False

        # по количеству оставшегося места в matrixXY
        if np.count_nonzero(matrixXY == 0) < paralX * paralY:
            recFindPlace(self, currentParal, beginZ + 1)

        for rowIndex in range(len(matrixXY)):
            row = np.array(matrixXY[rowIndex])

            # по свободному месту в ряду по X
            if row.sum() < paralX:
                continue

            # если объект не вместится по Y
            if len(matrixXY) - rowIndex < paralY:
                recFindPlace(self, currentParal, beginZ + 1)

            # если проверки пройдены
            for colIndex in range(len(matrixXY[0])):
                # находим свободную ячейку
                if matrixXY[rowIndex, colIndex] == 0:
                    col = np.array(matrixXY[colIndex])

                    # если свободных ячеек осталось меньше чем длина объекта
                    if np.count_nonzero(col[colIndex:] == 0) < paralX:
                        break


                pass

        # подтверждаем, что в этом месте paralY и paralZ свободных ячеек
        # вставляем объект на плоскость и записываем его данные в матрицы

        pass
