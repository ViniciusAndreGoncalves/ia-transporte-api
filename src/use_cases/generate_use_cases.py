from src.services.algorithms import Kruskal, AStar, GeneticAlgorithm
from src.services.initalize import graphs

from src.services.graphs import GraphService

class GenerateUseCases:
    def __init__(self):
        self.graph_service = GraphService()

    def generate_routes(self):
        # Implement the logic to generate routes using the algorithms
        kruskal = Kruskal(self.graph_service)
        a_star = AStar(self.graph_service)
        genetic_algorithm = GeneticAlgorithm(self.graph_service)
        

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
        self.graph_service.load()        
        # kruskal = Kruskal(*self.graph_service.create_graph())
        vertex, edges = self.graph_service.create_graph()
        kruskal = Kruskal(vertex, edges)
               
        
        kruskal.run()
        mst = kruskal.generate()
        # self.graph_service.save(mst)

        return mst