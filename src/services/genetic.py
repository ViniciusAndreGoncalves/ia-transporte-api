from collections import defaultdict
import numpy as np
import random

from src.services.a_star import AStarTrail
from src.services.graphs import GraphService

class GeneticAlgorithm:
    def __init__(self, population_size=200, mutation_rate=0.11, crossover_rate=0.92, generations=100, chromosome_lenght=51):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.generations = generations
        self.chromosome_lenght = chromosome_lenght

        self.graph_service = GraphService()

        self.maximum_cost = self.graph_service.get_graph("./src/public/kruskal_graph.json", False)[2] * 0.6

        self.astar = AStarTrail()

        self.fitness_memory = {}
        self.graph_edges, self.graph_dists = self.load_edges()

        self.common_routes = self.graph_service.get_most_common_rotes()
        self.loads_sum = sum([item[2] for item in self.common_routes])

    def load_edges(self):
        edges = []
        dists = []
        for edge in self.astar.edges:
            edges.append((edge['origem'], edge['destino']))
            dists.append(edge['distancia'])

        return edges, dists

    def init_population(self):
        return np.random.randint(0, 2, size=(self.population_size, self.chromosome_lenght), dtype=np.int8)

    def build_graph(self, active_index):
        trail_vertex = defaultdict(dict)
        for i in active_index:
            estate1, estate2 = self.graph_edges[i]

            trail_vertex[estate1][estate2]= self.graph_dists[i]
            trail_vertex[estate2][estate1]= self.graph_dists[i]

        return trail_vertex
    
    def calc_fitness(self, individual):
        ind_key = tuple(individual)
        if ind_key not in self.fitness_memory:            
            fit = 0

            active_index = np.where(individual == 1)[0]

            ind_cost = sum([self.graph_dists[i] for i in active_index]) * 2000000
            
            self.astar.trail_vertex = self.build_graph(active_index)
            for start, end, loads in self.common_routes:
                fit += self.astar.findpath(start, end)["cost"] * loads
            fit /= self.loads_sum

            if ind_cost > self.maximum_cost:
                penalization = ((ind_cost - self.maximum_cost)/(20000 * 51))
                fit += penalization
            else:
                penalization = ((ind_cost - self.maximum_cost)/(2000000 * 51))
                fit += penalization

            self.fitness_memory[ind_key] = fit
            
        return self.fitness_memory[ind_key]

    def crossover(self, parent1, parent2):
        if random.random() < self.crossover_rate:
            cross_point = random.randint(1, self.chromosome_lenght - 1)
            children1 = np.concatenate((parent1[:cross_point], parent2[cross_point:]))
            children2 = np.concatenate((parent1[cross_point:], parent2[:cross_point]))
            return children1, children2
        return parent1.copy(), parent2.copy()

    def tournament_selection(self, population, fitnesses, n_winners, k= 3):
        competitor_index = np.random.randint(0, len(population), size=(n_winners, k))
        tournament_fitness = fitnesses[competitor_index]
        tour_winners_index = np.argmin(tournament_fitness, axis=1)
        winners_index = competitor_index[np.arange(n_winners), tour_winners_index]

        return population[winners_index]

    def mutation(self, individual):
        for i in range(len(individual)):
            if random.random() < self.mutation_rate:
                individual[i] = 1 - individual[i]

    def show_gen(self, gen, fit):
        print(f"\nGen {gen}:")
        for i in range(len(fit)):
            print(f"\tInd {i}: {fit[i]}")

    def build_edges(self, vertex):
        pass

    def calc_graph_cost(self, ind):
        active_index = np.where(ind == 1)[0]
        return sum([self.graph_dists[i] for i in active_index]) * 2000000

    def create_genetic_graph(self, ind):
        graph = {}
        active_index = np.where(ind == 1)[0]
        graph['lista_adjacencias'] = self.build_graph(active_index)

        graph['total_cost'] = self.calc_graph_cost(ind)
        return graph

    def execute(self):
        population = self.init_population()
        best_results = []

        for generation in range(self.generations):
            fitnesses = []

            best_fit = (-1, float("inf"))
            for i, ind in enumerate(population):
                fit = self.calc_fitness(ind)
                fitnesses.append(fit)
                if fit < best_fit[1]:
                    best_fit = (i, fit)

            best_results.append(best_fit[1])
            best_ind = population[best_fit[0]]

            self.show_gen(generation, fitnesses)
            fitnesses = np.array(fitnesses)

            nw_gen = [best_ind] # Elitism

            while len(nw_gen) < self.population_size:
                parent1, parent2 = self.tournament_selection(population, fitnesses, 2)

                children1, children2 = self.crossover(parent1, parent2)
                self.mutation(children1)
                self.mutation(children2)

                nw_gen.extend([children1, children2])

            population = np.array(nw_gen)
            print(f'\tBest fitness:{best_fit}')

        return self.create_genetic_graph(best_ind)