from abc import ABC

from services.graphs import GraphService

class AStar(ABC):
    """Implementação do algoritmo A* para encontrar o caminho mais curto 
    entre duas capitais em um grafo."""
    def __init__(self):
        self.graph = GraphService()
        self.graph.load()
        self.vertex, self.edges = self.graph.get_graph()
        
        self.graph.load(filepath=f"./src/public/a_star_graph.json")
        self.heuristic = self.graph.get_graph_a_star()
        
        self.cost_road = 5         


    def findpath(self, start, goal):        

        # Lista para percorrer o grafo
        open_set = []

        # Um nó que vai receber o nó final do caminho - destino
        result = None

        # Econtra a capital no open_set com o menor f_score
        current = Node(is_road=None, state=start, state_father=None)
        open_set.append(current)
        
        while open_set:
            open_set = self._get_neighbors(current, open_set, goal)
            current = min(open_set, key=lambda node: node.f_score)
            if current.state == goal:
                result = current
                break

        self.get_path(result)


    def get_path(self, node):
        path = []

        while node is not None:              
            path.insert(0, node.state)
            node = node.state_father

        return path
        
                
    def _get_neighbors(self, current, open_set, goal):
        """
        Busca os vizinho do no atual do grafo a ser montado
        Retorna cada nó e a distância entre o nó atual e o vizinho
        """
        neighbors = self.vertex.get(current.state, [])

        # Verifica se o vizinho já foi visitado no caminho atual
        for neighbor in neighbors:
            if current.father == None or not self.is_visited(neighbor, current.father):
                new = Node(is_road=True, state=neighbor, state_father=current, g_score=0, h_score=self.calc_heuristics(current, goal))
                open_set.append(new)                

        return open_set
    
    
    def calc_heuristics(self, current, goal):
        """
        Essa função retorna a heurística, um dicionário(início) dentro de outro dicionário(destino)
        "MS": {
            "SE": 2155,
            ...
        return [MS][SE] = 2155
        """
        return self.heuristic[current][goal]        
    
    
    def is_visited(self, neighbor, node):
        """
        Verifica se o vizinho já foi visitado no caminho atual
        """
        while node is not None:
            if neighbor.state == node.state:
                return True
            node = node.state_father
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
    
    def calc_cost(self, distance):
        raise NotImplementedError("Subclasses devem implementar o método calc_cost")
    

class Node():
    def __init__(self, is_road=None, state=None, state_father=None, g_score=None, h_score=None):
        self.is_road = is_road
        self.state = state
        self.state_father = state_father
        self.g_score = g_score
        self.f_score = g_score + h_score


class AStarRoad(AStar):
    def calc_cost(self, distance):
        return distance * self.cost_road
    
    
    def calc_heuristics(self, current, goal):
        return self.heuristic[current][goal] * 5
    

class AStarTrail(AStar):
    def __init__(self):
        super().__init__()
        self.cost_trail = 1.2

    def calc_cost(self, distance):
        trail = True

        if trail:
            return distance * self.cost_trail
        else:
            return distance * self.cost_road
        
    
    def calc_heuristics(self, current, goal):
        return self.heuristic[current][goal] * 1.2