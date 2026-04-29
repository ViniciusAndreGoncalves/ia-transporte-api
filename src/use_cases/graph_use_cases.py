from src.services.graphs import GraphService

class GraphUseCase:
    def __init__(self):
        self.graph_service = GraphService()

    def get_graph(self):
        graph = {}
        vertex, edges, _ = self.graph_service.get_graph("./src/public/base_graph.json", False)
        
        graph["lista_adjacencias"] = vertex
        graph["lista_arestas"] = edges
        return graph
    
    def get_graph_kruskal(self):
        graph = {}
        vertex, edges, cost = self.graph_service.get_graph("./src/public/kruskal_graph.json", False)

        graph["lista_adjacencias"] = vertex
        graph["lista_arestas"] = edges
        graph["total_cost"] = cost
        return graph

    def get_graph_genetico(self):
        pass