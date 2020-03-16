import numpy as np
from extensionsFuncs import *


# Алгоритм упаковки First Fit - укладывает объект в первое попавшееся свободное место
def firstFit(self, currentParal, flag):
    if not self.allDict['matrixXY'].any():
        createMatrixes(self)

    if currentParal < len(self.allDict['parals']):
        print('currentParal:', currentParal, self.allParals[self.allDict['parals'][currentParal]])
    else:
        print('currentParal:', currentParal)
    recFF(self, currentParal, flag)


# Рекурсивная вставка объекта в свободную область
def recFF(self, currentParal, flag):
    window = self.ui.gl
    if currentParal < len(self.allDict['parals']):
        matrixXY = np.array(self.allDict['matrixXY'])

        paral = self.allDict['parals'][currentParal]
        (paralX, paralY, paralZ) = self.allParals[paral]

        # если в области еще нет объектов
        if matrixXY.sum() == 0:
            window.addItem(paral)
            self.allDict['placedParals'].append(paral)

            for i in range(paralX):
                for j in range(paralY):
                    matrixXY[i, j] = 1

            print(matrixXY, '\n')

            self.allDict['matrixXY'] = matrixXY
            self.allDict['matrixOfMatrices'].append(matrixXY)
            currentParal += 1
            self.allDict['currentParal'] = currentParal
            if not flag:
                recFF(self, currentParal, flag)

        # если в области есть объекты, то нужно искать для него место
        else:
            recFindPlace(self, currentParal, 0, 0)

            currentParal += 1
            self.allDict['currentParal'] = currentParal
            if not flag:
                recFF(self, currentParal, flag)


# Рекурсивный поиск свободного места во всех слоях рассматриваемой области
def recFindPlace(self, currentParal, beginI, beginJ):
    paral = self.allDict['parals'][currentParal]
    (paralX, paralY, paralZ) = self.allParals[paral]
    matrixXY = np.array(self.allDict['matrixXY'])

    currentJ = 0
    counter = 0
    for i in range(beginI, len(matrixXY)):
        # если есть место для объекта
        if len(matrixXY[i]) - matrixXY[i].sum() < paralX:
            continue

        # если длина объекта больше, чем длина оставшейся зоны поиска
        if len(matrixXY) - i - 1 < paralX:
            print('Для paral num.' + str(currentParal), 'с параметрами: (' + str(paralX) + ', ' + str(paralY) + ')',
                  'не хватает места\n')
            return False

        flag = False
        if beginI != 0 and i != beginI:
            beginJ = 0

        # проверяем, есть ли свободное место для объекта
        for j in range(beginJ, len(matrixXY[0])):
            # print('i =', i, 'j =', j, 'matrixXY[i]:', matrixXY[i], 'matrixXY[i][j:paralY + j]:',
            #       matrixXY[i][j:paralY + j])

            # если нашли свободную ячеку, то приступаем к проверке остальных свободных ячеек
            if matrixXY[i, j] == 0:
                # если таких свободных ячеек меньше, чем ширина объекта
                if len(matrixXY[i][j:]) < paralY or matrixXY[i][j:paralY + j].sum() != 0:
                    flag = True  # ставим флаг на выход
                    break
                else:
                    currentJ = j  # запоминаем текуший j
                    break

        if flag:  # ищем свободное место на следующем i
            continue

        # проверяем каждый столбец на наличие свободных ячеек
        for yy in range(paralY):
            # выбираем промежуток столбца равный длине объекта по X
            col = np.array(matrixXY[:, currentJ][i + yy:paralX + i])

            # print('col (matrixXY[:, currentJ][i + y:paralX]):', matrixXY[:, currentJ][i + y:paralX + i])

            # если все ячейки выбранного промежутка свободны, то увеличиваем счетчик
            if col.sum() == 0:
                counter += 1

            # если значение счетчика равно длине объекта по Y
            if counter == paralY:
                window = self.ui.gl
                self.allDict['allTranslations'][paral] = (i, currentJ, 0)
                paral.translate(i, currentJ, 0)
                window.addItem(paral)
                self.allDict['placedParals'].append(paral)

                for x in range(i, paralX + i):
                    for y in range(currentJ, paralY + currentJ):
                        matrixXY[x, y] = 1

                self.allDict['matrixXY'] = matrixXY
                self.allDict['matrixOfMatrices'].append(matrixXY)

                # print('currentParal =', currentParal, ';', paralX, paralY)

                print(matrixXY, '\n')

                return True
