import json
import os
import csv

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
            cost = 0 
            vertex = graph_return["lista_adjacencias"]
            edges = graph_return["lista_arestas"]
            if "total_cost" in graph_return:
                cost = graph_return["total_cost"]
            return vertex, edges, cost
    
    def get_most_common_rotes(self):
        common_rotes = []

        with open("./src/public/most_common_routes.csv", mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                common_rotes.append((row[1], row[2], int(row[3])))
        
        return common_rotes

    def save(self, data, filename):

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
