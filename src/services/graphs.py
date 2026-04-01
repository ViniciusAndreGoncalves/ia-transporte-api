import json

class GraphService:
    def __init__(self):
        self.data_graph = None

    def load(self, filepath="./src/public/base_graph.json"):
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                self.data_graph = json.load(file)
            print("Grafo carregado com sucesso.")
        except FileNotFoundError:
            print(f"Arquivo {filepath} não encontrado")
        except json.JSONDecodeError:
            print(f"Falha ao decodificar arquivo JSON: {filepath}")

    def create_graph(self):
        if not self.data_graph:
            raise ValueError("Grafo não carregado. Por favor, carregue um grafo antes de criar.")
        
        vertex = list(self.data_graph["lista_adjacencias"].keys())

        edges = self.data_graph["lista_arestas"]

        return vertex, edges
