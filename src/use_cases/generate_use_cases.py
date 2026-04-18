from src.services.kruskal import Kruskal
from src.services.initalize import graphs

from src.services.graphs import GraphService

class GenerateUseCases:
    def __init__(self):
        self.graph_service = GraphService()
    
    def generate_kruskal(self):
        """
        Gera a árvore geradora mínima usando o algoritmo de Kruskal e 
        salva o resultado em um arquivo JSON.
        """
        self.graph_service.load()        
        # kruskal = Kruskal(*self.graph_service.create_graph())
        vertex, edges = self.graph_service.get_graph()
        kruskal = Kruskal(vertex, edges)
        
        kruskal.run()
        mst = kruskal.generate()
        self.graph_service.save(mst)

        return mst