from src.services.genetic import GeneticAlgorithm
from src.services.graphs import GraphService
from src.services.kruskal import Kruskal


class GenerateUseCases:
    def __init__(self):
        self.graph_service = GraphService()
    
    def generate_kruskal(self):
        """
        Gera a árvore geradora mínima usando o algoritmo de Kruskal e 
        salva o resultado em um arquivo JSON.
        """
        vertex, edges, _ = self.graph_service.get_graph("./src/public/base_graph.json", False)
        kruskal = Kruskal(vertex, edges)
        
        result = kruskal.run()
        self.graph_service.save(result)

        return result
    
    def generate_genetic(self, population_size, mutation_rate, crossover_rate, generations):
        genetic = GeneticAlgorithm(population_size, mutation_rate, crossover_rate, generations)
        result = genetic.execute()
        return result