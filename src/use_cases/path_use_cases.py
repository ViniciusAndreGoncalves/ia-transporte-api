from services.a_star import AStarRoad, AStarTrail

class PathUseCases:
    """
    Recebe a requisição do front com início e o destino e retorna a lista com o caminho. API - Serviço
    """
    def __init__(self):
        pass

    def find_path(self, start, end):
        return AStarRoad().findpath(start, end)
    
    def find_path_kruskal(self, start, end):
        return AStarTrail().findpath(start, end)
    
    def find_path_genetico(self, start, end):
        pass