from fits2 import *
from random import shuffle, randint
import matplotlib.pyplot as plt


def printAll(obj):
    print('\n'.join(str(e) for e in obj))
    print()


def clearAll(self):
    self.allDict['placedParals'] = list()
    self.allDict['matrices'] = list()
    self.allDict['matrixOfMatrices'] = list()
    self.allDict['currentParal'] = 0
    self.allDict['allTranslations'] = dict()


# скрещивание
def crossing(population, parent_number):
    crossed_population = []

    # случайно выбираем родителей
    for _ in range(parent_number):
        shuffle(population)
        parent1 = list(population[0])
        parent2 = list(population[1])

        used_parals = []
        final_individual = []
        for i in range(len(parent1)):
            ind1 = list(parent1[i])
            ind2 = list(parent2[i])

            if ind1[0] not in used_parals:
                final_individual.append(list(ind1))
                used_parals.append(ind1[0])

            if ind2[0] not in used_parals:
                final_individual.append(list(ind2))
                used_parals.append(ind2[0])

        crossed_population.append(list(final_individual))

    return crossed_population


# фитнес-функция, где целевая функция - оставшееся место. Чем меньше - тем лучше
def fitnessFunction(self, individual: list):
    objects = list([paral[0] for paral in individual])
    parals = []
    for paral_obj in self.allDict['placedParals']:
        ind = list(individual)
        parals.append(ind[objects.index(paral_obj)])

    parals = [(paral[0], paral[1], paral[2], paral[3], paral[4], 0) for paral in parals]

    # parals = [(paral[0], paral[1], paral[2], paral[3], paral[4],
    #            self.allDict['maxSpace'] - sum([paral[-2] for paral in parals])) for paral in individual]
    parals = [(paral[0], paral[1], paral[2], paral[3], paral[4],
               sum([paral[-2] for paral in parals]) / self.allDict['maxSpace']) for paral in individual]

    return parals


# отбор - 1 лучшая особь, 80% из турнирки, остальные - счастливчики
def selection(self, population, ind_number):
    fitnessed_population = []

    for individual in population:
        clearAll(self)
        self.allDict['parals'] = list([paral[0] for paral in individual])
        self.allDict['is_show_parals'] = False
        firstFit(self, False)
        fitnessed_population.append(fitnessFunction(self, individual))

    selected_population = []
    # турнирная селекция
    for _ in range(ind_number):
        shuffle(fitnessed_population)
        ind1 = list(fitnessed_population.pop())
        ind2 = list(fitnessed_population.pop())

        if ind1[0][-1] >= ind2[0][-1]:
            selected_population.append(ind1)
        else:
            selected_population.append(ind2)

    return selected_population


# мутация
def mutation(population, mutation_number):
    for individual in population:
        if randint(0, 99) < mutation_number:
            i = randint(0, len(individual) - 1)
            j = i
            while j == i:
                j = randint(0, len(individual) - 1)

            individual[i], individual[j] = individual[j], individual[i]

    return population


# встряска
def shake(self):
    pass


def firstPopulation(self, ind_number):
    population = [self.allDict['paral_dict'] for _ in range(ind_number)]
    shuffled_population = []

    # перемешиваем первую популяцию
    for individual in population:
        shuffle(individual)
        shuffled_population.append(list(individual))

    return shuffled_population


def findBestInPopulation(population):
    # print([individual[0][-1] for individual in population])

    return population[np.argmin(np.array([individual[0][-1] for individual in population]))], np.min(np.array([individual[0][-1] for individual in population]))


def geneticAlgorithm(self):
    number_of_iteration = self.allDict['number_of_iteration']  # количество итераций генетического алгоритма
    ind_number = 10  # количество особей в каждой популяции
    crossed_number = ind_number * 10  # количество особей после размножения
    mutation_number = 10  # шанс мутации (в %)
    population = firstPopulation(self, ind_number)  # генерация первой популяции

    x = []
    y = []
    for i in range(number_of_iteration):
        # print('i =', i)
        x.append(i + 1)
        crossed_population = crossing(population, crossed_number)
        selected_population = selection(self, crossed_population, ind_number)
        population = list(mutation(selected_population, mutation_number))
        # print(findBestInPopulation(population), '\n')
        y.append(findBestInPopulation(population)[1])

        if self.allDict['best_value'] == .0:
            self.allDict['best_individual'] = list(findBestInPopulation(population)[0])
            self.allDict['best_value'] = findBestInPopulation(population)[1]
        else:
            if self.allDict['best_value'] < findBestInPopulation(population)[1]:
                self.allDict['best_individual'] = list(findBestInPopulation(population)[0])
                self.allDict['best_value'] = findBestInPopulation(population)[1]

    print('finalMin:')
    print(self.allDict['best_value'], '\n')
    printAll(self.allDict['best_individual'])

    clearAll(self)
    self.allDict['parals'] = [individual[0] for individual in self.allDict['best_individual']]
    self.allDict['is_show_parals'] = True
    preparingForFF(self, False)
    firstFit(self, False)

    plt.plot(x, y)
    plt.xlabel('Количество популяций')
    plt.ylabel('Занимаемый объем / объем контейнера')
    plt.show()
