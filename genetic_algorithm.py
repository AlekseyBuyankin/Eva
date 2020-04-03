from fits2 import *
from random import shuffle, randint
from numba import jit


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
def crossing(self, population, parent_number):
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

    fitnessed_population = []
    for individual in crossed_population:
        clearAll(self)
        self.allDict['parals'] = list([paral[0] for paral in individual])
        self.allDict['is_show_parals'] = False
        firstFit(self, False)
        fitnessed_population.append(fitnessFunction(self, individual))

    return fitnessed_population


# фитнес-функция, где целевая функция - занимаемый объем / объем контейнера.
# Чем больше - тем лучше
def fitnessFunction(self, individual: list):
    objects = list([paral[0] for paral in individual])
    parals = []
    for paral_obj in self.allDict['placedParals']:
        ind = list(individual)
        parals.append(ind[objects.index(paral_obj)])

    parals = [(paral[0], paral[1], paral[2], paral[3], paral[4], 0) for paral in parals]

    parals = [(paral[0], paral[1], paral[2], paral[3], paral[4],
               sum([paral[-2] for paral in parals]) / self.allDict['maxSpace']) for paral in individual]

    return parals


# отбор - 1 лучшая особь, 80% из турнирки, остальные - счастливчики
def selection(self, population, ind_number):
    fitnessed_population = []

    # вычисляем (занимаемый объем / объем контейнера) для каждой особи
    for individual in population:
        clearAll(self)
        self.allDict['parals'] = list([paral[0] for paral in individual])
        firstFit(self, False)
        fitnessed_population.append(fitnessFunction(self, individual))

    selected_population = []

    tournaments_number = int(ind_number * 0.7)
    lucker_number = ind_number - tournaments_number - 1

    # турнирная селекция
    replica = list(fitnessed_population)
    for _ in range(tournaments_number):
        shuffle(replica)
        ind1 = list(replica[0])
        ind2 = list(replica[1])

        if ind1[0][-1] >= ind2[0][-1]:
            selected_population.append(ind1)
        else:
            selected_population.append(ind2)

    # отбор счастливчиков
    for _ in range(lucker_number):
        shuffle(fitnessed_population)
        selected_population.append(fitnessed_population[0])

    # добавление 1 лучшего в популяции
    selected_population.append(findBestInPopulation(fitnessed_population)[0])

    return selected_population


# мутация
def mutation(population, mutation_probability):
    for individual in population:
        if randint(0, 99) < mutation_probability:
            i = randint(0, len(individual) - 1)
            j = i
            while j == i:
                j = randint(0, len(individual) - 1)

            individual[i], individual[j] = individual[j], individual[i]

    return population


# встряска
def shake(population):
    survival_number = int(len(population) * 0.3)

    shuffle(population)
    # оставляем 1/3 поколения, остальная не выживает
    new_population = list(population[0: survival_number])
    random_number = len(population) - len(new_population)

    # набираем новое поколение из случайных особей
    for _ in range(random_number):
        shuffle(population)
        individual = population[0]
        shuffle(individual)

        new_population.append(individual)

    return new_population


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

    return population[np.argmin(np.array([individual[0][-1] for individual in population]))], np.min(
        np.array([individual[0][-1] for individual in population]))

def geneticAlgorithm(self):
    number_of_iteration = self.allDict['number_of_iteration']  # количество итераций генетического алгоритма
    self.allDict['ind_number'] = ind_number = 100  # количество особей в каждой популяции
    self.allDict['selected_number'] = selected_number = ind_number // 10  # количество особей после отбора
    self.allDict['crossed_number'] = crossed_number = ind_number  # количество особей после размножения
    self.allDict['mutation_probability'] = mutation_probability = 10  # шанс мутации (в %)

    population = firstPopulation(self, ind_number)  # генерация первой популяции

    x = []
    y = []
    shake_buff = []
    values = []
    for i in range(number_of_iteration + 1):
        # if i % 10 == 0:
        # print('i =', i)

        selected_population = selection(self, population, selected_number)
        crossed_population = crossing(self, selected_population, crossed_number)
        population = mutation(crossed_population, mutation_probability)

        best_individual = findBestInPopulation(population)[0]
        best_value = findBestInPopulation(population)[1]

        if not shake_buff:
            shake_buff.append(best_value)
        else:
            if best_value == shake_buff[0]:
                if len(shake_buff) < 2:
                    shake_buff.append(best_value)
                else:
                    population = shake(population)
                    best_individual = findBestInPopulation(population)[0]
                    best_value = findBestInPopulation(population)[1]
                    shake_buff = [best_value]
            else:
                shake_buff = [best_value]

        # if len(y) >= 1:
        #     if best_value > y[-1]:
        #         x.append(i + 1)
        #         y.append(best_value)
        # else:
        #     x.append(i + 1)
        #     y.append(best_value)

        if i % 10 == 0:
            print('i =', i)
            x.append(i + 1)
            if i == 0:
                y.append(best_value)
            else:
                y.append(np.max(values))
            values = []
        else:
            values.append(best_value)

        if self.allDict['best_value'] == .0:
            self.allDict['best_individual'] = list(best_individual)
            self.allDict['best_value'] = best_value
        else:
            if self.allDict['best_value'] < best_value:
                self.allDict['best_individual'] = list(best_individual)
                self.allDict['best_value'] = best_value

    # print('finalMin:')
    # print(self.allDict['best_value'], '\n')

    # x.append(number_of_iteration)
    # y.append(self.allDict['best_value'])
    # printAll(self.allDict['best_individual'])

    clearAll(self)
    self.allDict['parals'] = [individual[0] for individual in self.allDict['best_individual']]
    self.allDict['is_show_parals'] = True
    preparingForFF(self, False)
    firstFit(self, False)
    self.allDict['is_show_parals'] = False

    # plt.plot(x, y)
    # plt.xlabel('Количество популяций')
    # plt.ylabel('Значение целевой функции')
    # plt.show()

    print('Генетический алгоритм закончил работу.\n')
    return x, y
