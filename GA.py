import random

import Population as p
import Schedule as s

POPULATION_NUM = 9  # population number
k = 3  # number of tournament candidates
mutation_rate = 0.01
cross_rate = 0.1  # number of retained population from last generation


class GeneticAlgorithm:

    def _tournament_selection(self, population):
        tournament_population = p.Population(0)
        for _ in range(k):
            tournament_population.get_schedules().append(
                population.get_schedules()[random.randrange(0, POPULATION_NUM)])
        tournament_population.get_schedules().sort(key=lambda x: x.get_fitness(),reverse= True)
        return tournament_population

    def _crossover_population(self, population):
        crossover_population = p.Population(0)
        elite_count = round(len(population.get_schedules()) * cross_rate)
        crossover_population.get_schedules().append(
            population.get_schedules()[:elite_count])
        for _ in range(elite_count, POPULATION_NUM):
            sched1 = self._tournament_selection(population).get_schedules()[0]
            sched2 = self._tournament_selection(population).get_schedules()[0]
            crossover_population.get_schedules().append(self._crossover(sched1, sched2))
        return crossover_population

    def _crossover(self, parent1, parent2):
        child = s.Schedule().initialization()
        for i in range(len(child.get_classes())):
            if random.random() > 0.5:
                child.get_classes()[i] = parent1.get_classes()[i]
            else:
                child.get_classes()[i] = parent2.get_classes()[i]
        return child

    def _mutate_population(self, population):
        elite_count = round(len(population.get_schedules()) * cross_rate)
        for i in range(elite_count, POPULATION_NUM):
            self._mutate(population.get_schedules()[i])
        return population

    def _mutate(self, schedule):
        mutated_schedule = s.Schedule().initialization()
        for i in range(len(mutated_schedule.get_classes())):
            if (mutation_rate > random.random()):
                mutated_schedule.get_classes()[i] = schedule.get_classes()[i]
        return mutated_schedule

    def evolve(self, population):
        return self._mutate_population(self._crossover_population(population))