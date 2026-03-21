from services.algorithms import Kruskal, AStar, GeneticAlgorithm

class GenerateUseCases:
    def __init__(self, graph):
        self.graph = graph

    def generate_routes(self):
        # Implement the logic to generate routes using the algorithms
        kruskal = Kruskal(self.graph)
        a_star = AStar(self.graph)
        genetic_algorithm = GeneticAlgorithm(self.graph)
        

        # Example of how to use the algorithms (this is just a placeholder)
        kruskal_result = kruskal.generate()
        a_star_result = a_star.generate()
        genetic_algorithm_result = genetic_algorithm.generate()

        # Combine results or choose the best one based on your criteria
        return {
            "kruskal": kruskal_result,
            "a_star": a_star_result,
            "genetic_algorithm": genetic_algorithm_result
        }
    
    def generate_kruskal(self):
        kruskal = Kruskal(self.graph)
        return kruskal.generate()