from extensionsFuncs import *


def firstFit(self, flag):
    current_paral = self.allDict['currentParal']

    if not self.allDict['matrices']:
        createMatrices(self)

    if current_paral < len(self.allDict['parals']):
        # print('\nТекущий объект:', current_paral, 'с параметрами: ',
        #       self.allParals[self.allDict['parals'][current_paral]])
        recFF(self, flag)
    else:
        # print('Объекты кончились')
        pass


def firstFitDecreasing(self, flag):
    current_paral = self.allDict['currentParal']

    if not self.allDict['matrices']:
        createMatrices(self)

    if current_paral < len(self.allDict['parals']):
        # print('\nТекущий объект:', current_paral, 'с параметрами: ',
        #       self.allParals[self.allDict['parals'][current_paral]])
        recFF(self, flag)
    else:
        # print('Объекты кончились')
        pass


def recFF(self, flag):
    current_paral = self.allDict['currentParal']
    # если объект первый
    if current_paral == 0:
        paral = self.allDict['parals'][current_paral]
        (paralX, paralY, paralZ) = self.allParals[paral]
        window = self.ui.gl
        window.addItem(paral)
        self.allDict['placedParals'].append(paral)
        writeToAllMatrices(self, 0, 0, 0)
        self.allDict['matrixOfMatrices'].append(list(self.allDict['matrices']))
        # print('Объект', current_paral, (paralX, paralY, paralZ), 'упакован')

        self.allDict['currentParal'] += 1

        # printMatricesToString(self, 0, paralZ)

        if not flag:
            if not current_paral < len(self.allDict['parals']):
                return False
            else:
                recFF(self, flag)

    else:
        recFindPlace(self, 0)

        if not flag:
            if not current_paral < len(self.allDict['parals']):
                return False
            else:
                recFF(self, flag)


def recFindPlace(self, beginZ):
    matrices = self.allDict['matrices']
    current_paral = self.allDict['currentParal']

    # print('Слой #' + str(beginZ))
    # print('Матрицы до:')
    # printAllMatrices(self)

    if beginZ < len(matrices) and current_paral < len(self.allDict['parals']):
        # переменные
        paral = self.allDict['parals'][current_paral]
        (paralX, paralY, paralZ) = self.allParals[paral]
        matrixXY = matrices[beginZ]

        # проверяем легкими проверками на свободное место
        # по высоте
        if paralZ > len(matrices) - beginZ:
            # print('\nПроверка по высоте: нет места для объекта:', (paralX, paralY, paralZ))
            # print('Объект', current_paral, (paralX, paralY, paralZ), 'не был упакован')
            self.allDict['currentParal'] += 1
            return False

        # по количеству оставшегося места в matrixXY
        if np.count_nonzero(matrixXY == 0) < paralX * paralY:
            # print('Проверка по количеству оставшегося места в matrixXY\n')
            if recFindPlace(self, beginZ + 1):
                return True
            else:
                return False

        for rowIndex in range(len(matrixXY)):
            # print('rowIndex:', rowIndex, '\n')
            row = np.array(matrixXY[rowIndex])

            # по свободному месту в ряду по X (если свободных ячеек меньше чем длина объекта)
            if np.count_nonzero(row == 0) < paralX:
                # print('Проверка 1: по свободному месту в ряду по X', np.count_nonzero(row == 0), '<', paralX, '\n')
                continue

            # если объект не вместится по Y
            if len(matrixXY) - rowIndex < paralY:
                # print('Проверка 2: если объект не вместится по Y', len(matrixXY), '-', rowIndex, '<', paralY, '\n')
                if recFindPlace(self, beginZ + 1):
                    return True
                else:
                    return False

            # если легкие проверки пройдены
            for colIndex in range(len(matrixXY[0])):
                # находим свободную ячейку
                if matrixXY[rowIndex, colIndex] == 0:
                    col = np.array(matrixXY[:, colIndex])
                    # print('Нашел свободную ячейку', 'col =', col)

                    # если свободных ячеек осталось меньше чем длина объекта
                    if np.count_nonzero(col[colIndex:] == 0) < paralX:
                        # print('Проверка 3: если свободных ячеек осталось меньше чем длина объекта', col[colIndex:],
                        #       np.count_nonzero(col[colIndex:] == 0), '<', paralX)
                        break

                    # если случается неведомая фигня
                    if rowIndex + paralX > len(matrixXY[0]) or colIndex + paralY > len(matrixXY):
                        # print('Проверка 4: если случается неведомая фигня')
                        # print(rowIndex, '+', paralX, '>', len(matrixXY[0]), 'and', colIndex, '+', paralY, '>',
                        #       len(matrixXY))
                        break

                    # если свободных ячеек по Y меньше чем ширина объета
                    if np.count_nonzero(row[colIndex: colIndex + paralY] == 0) != paralY:
                        # print(row[colIndex: colIndex + paralY],
                        #       np.count_nonzero(row[colIndex: colIndex + paralY] == 0),
                        #       '!=', paralY)
                        break

                    # подтверждаем или опровергаем, что в этом месте paralX, paralY,  paralZ свободных ячеек
                    if isAvailableXYZ(self, rowIndex, colIndex, beginZ):
                        self.allDict['allTranslations'][paral] = (rowIndex, colIndex, beginZ)
                        paral.translate(rowIndex, colIndex, beginZ)
                        window = self.ui.gl
                        # вставляем объект на плоскость
                        window.addItem(paral)
                        self.allDict['placedParals'].append(paral)
                        # записываем данные объекта в матрицы
                        writeToAllMatrices(self, rowIndex, colIndex, beginZ)

                        # print('Слой:', beginZ)
                        # print('Матрицы после:')
                        # printAllMatrices(self)
                        # print('------------------------------------------------------------------------------')
                        #
                        # print('Объект', current_paral, (paralX, paralY, paralZ), 'упакован')

                        self.allDict['matrixOfMatrices'].append(list(self.allDict['matrices']))
                        self.allDict['currentParal'] += 1

                        return True

        # print('Объект не нашел свободного места на этом уровне')
        if recFindPlace(self, beginZ + 1):
            return True
        else:
            return False
    else:
        return False
