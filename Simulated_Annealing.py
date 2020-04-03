from random import shuffle, random
from genetic_algorithm import printAll, clearAll
from fits2 import firstFit
from math import exp
import matplotlib.pyplot as plt
import numpy as np


class Simulated_Annealing:
    def __init__(self, allDict, allParals):
        self.allDict = allDict
        self.allParals = allParals

        self.Tstart = self.allDict['number_of_iteration']
        self.m = self.Tstart * 10
        self.Tend = 0.1
        self.ind_number = 10
        self.best_value = None

        self.individual = None
        self.new_individual = None
        self.energy = None
        self.new_energy = None

    def getFirstIndividual(self):
        individual = list(self.allDict['paral_dict'])
        shuffle(individual)
        self.individual = list(individual)

    def getNewIndividual(self):
        individual = list(self.individual)
        shuffle(individual)
        self.new_individual = list(individual)

    def getEnergy(self, individual):
        clearAll(self)
        self.allDict['parals'] = [paral[0] for paral in individual]
        firstFit(self, False)

        objects = list([paral[0] for paral in individual])
        parals = []
        for paral_obj in self.allDict['placedParals']:
            ind = list(individual)
            parals.append(ind[objects.index(paral_obj)])

        energy = sum([paral[-1] for paral in parals]) / self.allDict['maxSpace']

        return energy

    def main(self):
        s_a = Simulated_Annealing
        t = self.Tstart

        # задаем произвольное первое состояние s1
        s_a.getFirstIndividual(self)

        x = [0]
        y = [s_a.getEnergy(self, self.individual)]
        values = []
        for k in range(1, self.m):
            # вычисляем новую популяцию
            s_a.getNewIndividual(self)

            dE = s_a.getEnergy(self, self.new_individual) - s_a.getEnergy(self, self.individual)

            if dE <= 0:
                self.individual = list(self.new_individual)
            else:
                p = random()
                # print(p, exp(-dE / t))
                if p <= exp(-dE / t):
                    self.individual = list(self.new_individual)

            t = self.Tstart * .1 / k

            value = s_a.getEnergy(self, self.individual)

            # if len(y) >= 1:
            #     if value > y[-1]:
            #         x.append(k)
            #         y.append(value)
            #         self.best_value = value
            # else:
            #     x.append(k)
            #     y.append(value)
            #     self.best_value = value
            if k % 10 == 0 and k != 0:
                print('k =', k)
                x.append(k)
                y.append(np.max(values))
                values = []
            else:
                values.append(value)
            if t < self.Tend:
                break

        # x.append(self.Tstart)
        # y.append(self.best_value)

        # plt.plot(x, y)
        # plt.xlabel('Количество популяций')
        # plt.ylabel('Значение целевой функции')
        # plt.show()

        print('Алгоритм имитации отжига закончил работу.')
        return x, y
