from fits2 import *
from random import shuffle


def printAll(obj):
    print('\n'.join(str(e) for e in obj))
    print()


def clearAll(self):
    self.allDict['placedParals'] = list()
    self.allDict['matrices'] = list()
    self.allDict['matrixOfMatrices'] = list()
    self.allDict['currentParal'] = 0


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
    ps = list([paral[0] for paral in individual])
    parals = []
    for paral in self.allDict['placedParals']:
        parals.append(individual[ps.index(paral)])

    parals = [(paral[0], paral[1], paral[2], paral[3], paral[4],
               self.allDict['maxSpace'] - sum([paral[-1] for paral in parals])) for paral in individual]

    return parals


# отбор
def selection(self, population, ind_number):
    fitnessed_population = []

    for individual in population:
        clearAll(self)
        self.allDict['parals'] = list([paral[0] for paral in individual])
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
def mutation(population):


    pass


# супермутация
def superMutation(self):
    pass


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


def geneticAlgorithm(self):
    number_of_iteration = self.allDict['number_of_iteration']
    ind_number = 5
    crossed_number = ind_number * 2
    population = firstPopulation(self, ind_number)

    for _ in range(number_of_iteration):
        crossed_population = crossing(population, crossed_number)
        selected_population = selection(self, crossed_population, ind_number)

        mutation(selected_population)