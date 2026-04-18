import json
import os

class GraphService:
    def __init__(self):
        pass        

    def load(self, filepath="./src/public/base_graph.json"):
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                return json.load(file)
            print("Grafo carregado com sucesso.")
        except FileNotFoundError:
            print(f"Arquivo {filepath} não encontrado")
        except json.JSONDecodeError:
            print(f"Falha ao decodificar arquivo JSON: {filepath}")

    def get_graph(self, graph_path, is_heuristics):
        graph_return = self.load(graph_path)        
        if is_heuristics:
            return graph_return["lista_adjacencias"]
        else: 
            vertex = graph_return["lista_adjacencias"]
            edges = graph_return["lista_arestas"]
            return vertex, edges
    
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
