import numpy as np
import operator
from fits2 import firstFit
from extensionsFuncs import clearAll, printAll
from time import time
from tqdm import tqdm


def printObjects(obj):
    print('objects:')
    for i in obj:
        s = '['
        for g in i:
            s += str(g)[-5:-1] + ' '
        print(s[:-1] + ']')
    print('--')


class Generic_Algorithm:
    def __init__(self, allDict, allParals, number_of_generations, ind_number, elite, mutation_probability):
        self.allDict = allDict
        self.allParals = allParals
        self.number_of_generations = number_of_generations

        # self.ind_number = 15
        # self.elite = .1
        # self.mutation_probability = .001

        self.ind_number = ind_number
        self.elite = elite
        self.mutation_probability = mutation_probability

        self.individual = None
        self.population = None
        self.best_cost = None
        self.best_solution = None
        self.population_fitness = None

    def getFirstPopulation(self):
        population = [self.allDict['parals'] for _ in range(self.ind_number)]
        shuffled_population = []

        # перемешиваем первую популяцию
        for individual in population:
            np.random.shuffle(individual)
            np.random.shuffle(individual)
            np.random.shuffle(individual)
            shuffled_population.append(list(individual))

        self.population = shuffled_population

    def calculate_sol_cost(self, individual):
        parals = []

        for paral_obj in self.allDict['placedParals']:
            parals.append(individual[individual.index(paral_obj)])

        s = 0
        for paral in parals:
            x, y, z = self.allParals[paral]
            s += x * y * z

        return s

    def calculate_sol_fitness(self, sol):
        return self.calculate_sol_cost(sol) / self.allDict['maxSpace']

    def calculate_pop_fitness(self):
        fitness_results = {}

        # цикл для вычисления значения ЦФ для каждой хромосомы текущей популяции
        for i in range(len(self.population)):
            self.allDict['parals'] = self.population[i]
            clearAll(self)
            firstFit(self, False)
            fitness_results[i] = self.calculate_sol_fitness(self.population[i])

        self.population_fitness = sorted(fitness_results.items(), key=operator.itemgetter(1), reverse=True)

        l_best_solution = self.population[self.population_fitness[0][0]]
        self.update_stats(l_best_solution, self.population_fitness[0][1])

    def update_stats(self, l_best_solution, l_best_cost):
        if self.best_solution is None:
            self.best_solution = l_best_solution
            self.best_cost = l_best_cost

        elif self.best_cost < l_best_cost:
            self.best_solution = l_best_solution
            self.best_cost = l_best_cost

        self.best_solution = l_best_solution
        self.best_cost = l_best_cost

    def selection(self):
        new_population = []

        # добавление элит в популяцию
        elite_number = round(self.ind_number * self.elite)
        for i in range(elite_number):
            new_population.append(self.population[self.population_fitness[i][0]])

        # отбор особей для скрещивания
        t_size = np.random.randint(low=2, high=5)  # размер турнира
        p = 0.9  # вероятность попадания в турнир
        mating_pool = []  # скрещивающиеся особи

        n = 0
        while n < self.ind_number:
            solutions = []
            for i in range(t_size):
                solutions.append(self.population_fitness[np.random.randint(low=0, high=self.ind_number)])

            solutions.sort(key=lambda x: x[1])  # [(индекс, знач_цф)]

            for i in range(t_size):
                if n < self.ind_number:
                    if p * (1 - p) ** i >= np.random.uniform(low=0, high=1):
                        index = solutions[i][0]
                        parent = self.population[index]
                        mating_pool.append(parent)
                        n += 1
                else:
                    break

        # скрещивание особей. добавление новых особей в новое поколение
        n = elite_number
        while n < self.ind_number:
            parent1 = mating_pool[n - 1]
            parent2 = mating_pool[n]

            child1, child2 = self.crossover(parent1, parent2)
            new_population.append(child1)
            n += 1
            if n < self.ind_number:
                new_population.append(child2)
                n += 1

        self.population = new_population

    def crossover(self, parent1, parent2):
        n = len(parent1)

        # генерация позиций для скрещивания
        start = np.random.randint(0, n // 2)
        end = np.random.randint(n // 2 + 1, n - 1)

        # создание новых хромосом
        new_parent1 = []
        new_parent2 = []

        for i in range(start, end):
            new_parent1.append(parent1[i])  # 1я хромосома получает часть генов от 1й родительской
            new_parent2.append(parent2[i])  # 2я хромосома получает часть генов от 2й родительской
        used_np1 = list(new_parent1)
        used_np2 = list(new_parent2)

        for i in range(len(parent1)):
            if parent1[i] not in used_np2:
                new_parent2.append(parent1[i])
            else:
                used_np2.remove(parent1[i])

            if parent2[i] not in used_np1:
                new_parent1.append(parent2[i])
            else:
                used_np1.remove(parent2[i])

        return new_parent1, new_parent2

    def mutate_individual(self, sol):
        if np.random.random() <= self.mutation_probability:
            n = len(sol)
            a = np.random.randint(0, n - 1)
            b = np.random.randint(0, n - 1)
            while b == a:
                b = np.random.randint(0, n - 1)
            sol[a], sol[b] = sol[b], sol[a]

    def mutation(self):
        # цикл, запускающий мутацию текущей популяции
        for solution in self.population:
            self.mutate_individual(solution)

    def main(self):
        start = time()

        # создание первой популяции хромосом случайным образом
        self.getFirstPopulation()

        # вычисление приспособленности хромосом (ЦФ)
        self.calculate_pop_fitness()
        self.selection()

        x = [0]
        y = [self.best_cost]
        for i in tqdm(range(1, self.number_of_generations + 1)):
            self.selection()
            self.mutation()
            self.calculate_pop_fitness()
            x.append(i)
            y.append(self.best_cost)

        return self.best_cost, self.best_solution, time() - start
