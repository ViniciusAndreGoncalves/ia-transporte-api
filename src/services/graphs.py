import json
import os

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

    def get_graph(self):
        if not self.data_graph:
            raise ValueError("Grafo não carregado. Por favor, carregue um grafo antes de criar.")
        
        vertex = list(self.data_graph["lista_adjacencias"].keys())

        edges = self.data_graph["lista_arestas"]

        return vertex, edges
    
    def get_graph_a_star(self):
        if not self.data_graph:
            raise ValueError("Grafo não carregado. Por favor, carregue um grafo antes de criar.")
        
        vertex = list(self.data_graph["lista_adjacencias"].keys())

        return vertex
    
    def save(self, data, filename="kruskal_graph.json"):

        filepath = f"./src/public/{filename}"
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        try:
            with open(filepath, 'w', encoding='utf-8') as file:
                json.dump(
                    data, 
                    file,
                    ensure_ascii=False, # Permite caracteres acentuados
                    indent=4 # Escreve o JSON com indentação para melhor legibilidade
                )
            print(f"Dados salvos com sucesso em {filepath}.")
            return True
        except IOError as e:
            print(f"Erro ao salvar arquivo: {e}")
            return False
