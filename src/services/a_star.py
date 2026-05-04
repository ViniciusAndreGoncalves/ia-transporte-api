from abc import ABC
import heapq

from src.services.graphs import GraphService

class AStar(ABC):
    """Implementação do algoritmo A* para encontrar o caminho mais curto 
    entre duas capitais em um grafo."""
    def __init__(self):
        self.graph = GraphService()   
        self.vertex, self.edges, _ = self.graph.get_graph("./src/public/base_graph.json", False)
        self.heuristic = self.graph.get_graph("./src/public/a_star_graph.json", True)  
        self.cost_road = 5    


    def findpath(self, start, goal):        

        # Lista para percorrer o grafo
        open_set = []

        # Um nó que vai receber o nó final do caminho - destino
        result = None

        # Econtra a capital no open_set com o menor f_score
        current = Node(is_road=None, state=start, father=None)
        heapq.heappush(open_set, (current.f_score, current))
        
        while open_set:
            open_set = self._get_neighbors(current, open_set, goal)
            _, current = heapq.heappop(open_set) 
            if current.state == goal:
                result = current
                break

        # Retorna uma tupla, lista contendo o caminho percorrido e o resultado da soma das distâncias (g_score)
        return {
            "path": self.get_path(result), 
            "cost": result.g_score
            }


    def get_path(self, node):
        path = []

        while node.father is not None:         
            path.insert(0, (f"{node.father.state} - {node.state} - {"rodovia" if node.is_road else "ferrovia"}"))
            node = node.father

        return path
        
                
    def _get_neighbors(self, current, open_set, goal):
        """
        Busca os vizinhos do no atual do grafo a ser montado
        Retorna cada nó e a distância entre o nó atual e o vizinho
        """
        neighbors = self.vertex.get(current.state, [])        

        # Verifica se o vizinho já foi visitado no caminho atual
        for state_neighbor in neighbors:
            if current.father is None or not self.is_visited(state_neighbor, current.father):                
                new = Node(
                    is_road=True, 
                    state=state_neighbor, 
                    father=current, 
                    g_score=self.calc_cost(current.g_score, neighbors[state_neighbor]), 
                    h_score=self.calc_heuristics(current, goal))
                heapq.heappush(open_set, (new.f_score, new))

        return open_set
    
    
    def calc_cost(self, g_score_current, cost_neighbor):
        """
        Calcula o custo do caminho percorrido - g_score - g(h)
        """
        return cost_neighbor + g_score_current
    
    
    def calc_heuristics(self, current, goal):
        """
        Essa função retorna a heurística, um dicionário(início) dentro de outro dicionário(destino)
        "MS": {
            "SE": 2155,
            ...
        return [MS][SE] = 2155
        """
        return self.heuristic[current.state][goal]        
    
    
    def is_visited(self, neighbor, node):
        """
        Verifica se o vizinho já foi visitado no caminho atual
        """
        while node is not None:
            if neighbor == node.state:
                return True
            node = node.father
        return False


    def _reconstruct_path(self, came_from, current):
        """
        Reconstrói o caminho do nó inicial até o nó atual       
        """
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.append(current)

        total_path.reverse()
        return total_path
    

class Node():
    def __init__(self, is_road=None, state=None, father=None, g_score=0, h_score=0):
        self.is_road = is_road
        self.state = state
        self.father = father
        self.g_score = g_score
        self.f_score = g_score + h_score
    
    def __lt__(self, other):
        """
        Método mágico para o heapq funcionar. O heapq utiliza essa função para ordenar os nós.
        Basicamente ela verifica se o nó atual é o menor que o outro nó (distância - f_score).
        """
        return self.f_score < other.f_score
    
    def __str__(self):
        return f"State:{self.state}| g_score:{self.g_score}| f_score:{self.f_score}| is_road:{self.is_road}|father:{"None " if not self.father else self.father.state}"


class AStarRoad(AStar):
    def calc_cost(self, g_score_current, cost_neighbor):
        """
        Calcula o custo do caminho percorrido - g_score - g(h)
        cost_neighbor - custo do atual até o próximo
        g_score_current - custo total acumulado
        """
        return (cost_neighbor * self.cost_road) + g_score_current
    
    
    def calc_heuristics(self, current, goal):
        """
        Essa função retorna a heurística, um dicionário(início) dentro de outro dicionário(destino)
        "MS": {
            "SE": 2155,
            ...
        return [MS][SE] = 2155
        """
        return self.heuristic[current.state][goal] * 5
    

class AStarTrail(AStar):
    def __init__(self, trail_type):
        super().__init__()
        self.trail_graphs = {
            "kruskal":"./src/public/kruskal_graph.json",
            "genetic":"./src/public/genetic_graph.json"
        }
        self.trail_vertex, self.trail_edges, _ = self.graph.get_graph(self.trail_graphs[trail_type], False)
        self.cost_trail = 1.2

    def _get_neighbors(self, current, open_set, goal):
        """
        Busca os vizinhos do no atual do grafo a ser montado
        Retorna cada nó e a distância entre o nó atual e o vizinho
        """
        neighbors = self.vertex.get(current.state, [])        
        is_road = True
        
        # Verifica se o vizinho já foi visitado no caminho atual
        for state_neighbor in neighbors:
            if current.father is None or not self.is_visited(state_neighbor, current.father):                
                new = Node(
                    is_road=is_road, 
                    state=state_neighbor, 
                    father=current, 
                    g_score=self.calc_cost(
                        current, 
                        is_road, 
                        neighbors[state_neighbor], 
                        need_transhipment= False if current.is_road is None else current.is_road != is_road
                    ), 
                    h_score=self.calc_heuristics(state_neighbor, goal)
                )
                heapq.heappush(open_set, (new.f_score, new))

        trail_neighbors = self.trail_vertex.get(current.state, [])
        is_road=False        

        # Verifica se o vizinho já foi visitado no caminho atual
        for state_neighbor in trail_neighbors:
            if current.father is None or not self.is_visited(state_neighbor, current.father):                
                new = Node(
                    is_road=is_road, 
                    state=state_neighbor, 
                    father=current, 
                    g_score=self.calc_cost(
                        current, 
                        is_road, 
                        neighbors[state_neighbor], 
                        need_transhipment= False if current.is_road is None else current.is_road != is_road
                    ), 
                    h_score=self.calc_heuristics(state_neighbor, goal)
                )
                heapq.heappush(open_set, (new.f_score, new))

        return open_set

    def calc_cost(self, current, is_road, cost_neighbor, need_transhipment):
        """
        Calcula o custo do caminho percorrido - g_score - g(h)
        cost_neighbor - custo do atual até o próximo
        g_score_current - custo total acumulado
        """
        transhipment_cost = 1000 if need_transhipment else 0
        
        if is_road != need_transhipment:
            return (cost_neighbor * self.cost_road) + current.g_score + transhipment_cost
        else:
            return (cost_neighbor * self.cost_trail) + current.g_score + transhipment_cost
        
    def calc_heuristics(self, current, goal):
        return self.heuristic[current][goal] * self.cost_trail