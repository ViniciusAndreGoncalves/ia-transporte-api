from services.a_star import AStar, AStarRoad, AStarTrail

# Classe de teste para respostas no console

print(f"Rodovia: {AStarRoad().findpath("MS","DF")}")
print(f"Ferrovia: {AStarTrail().findpath("MS","DF")}")