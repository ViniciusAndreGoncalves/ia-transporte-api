class Kruskal:
    def __init__(self, vertex, edges):
        self.vertex = vertex
        self.edges = edges
        self.mst = []
        self.total_cost = 0
        self.father = {}
        self.rank = {}

    def run(self):
        
        for v in self.vertex:
            self.father[v] = v
            self.rank[v] = 0

        
        sorted_edges = sorted(self.edges, key=lambda item: item['distancia'])

        for edge in sorted_edges:
            u = edge['origem']
            v = edge['destino']
            cost = edge['distancia']

            
            if self.find(u) != self.find(v):
                self.union(u, v)
                self.mst.append(edge)
                self.total_cost += cost

        return {
            'minimum_spanning_tree': self.mst,
            'total_cost': self.total_cost
        }

    def find(self, i):
        if self.father [i] == i:
            return i
            
        self.father[i] = self.find(self.father[i])
        return self.father[i]

    def union(self, i, j):
            root_i = self.find(i)
            root_j = self.find(j)

            if root_i != root_j:
                if self.rank[root_i] < self.rank[root_j]:
                    self.father[root_i] = root_j
                elif self.rank[root_i] > self.rank[root_j]:
                    self.father[root_j] = root_i
                else:
                    self.father[root_j] = root_i
                    self.rank[root_i] += 1
    
    def display(self):
        print("\n--- Árvore Geradora Mínima ---")
        for aresta in self.mst:
            print(f"{aresta['origem']} -> {aresta['destino']} (Distância: {aresta['distancia']} km)")
        
        print(f"\nDistância Total para conectar todo o Brasil: {self.total_cost} km")

        

class AStar:
    def __init__(self, graph):
        pass

class GeneticAlgorithm:
    def __init__(self, graph):
        pass