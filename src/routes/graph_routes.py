from fastapi import APIRouter, Depends
from src.use_cases.graph_use_cases import GraphUseCase


router = APIRouter(prefix="/grafo", tags=["Grafos"])

graph_use_case = GraphUseCase()

@router.get("/")
def get_graph():
    """Essa rota fica responsável por retornar a rota da rodovia."""
    result = graph_use_case.get_graph()

    return result

"""Ambas rotas abaixo são responsáveis por retornar a rota das ferrovias."""
@router.get("/kruskal")
def get_graph_kruskal():
    result = graph_use_case.get_graph_kruskal()

    return result

@router.get("/genetico")
def get_graph_genetico():
    result = graph_use_case.get_graph_genetico()
    
    return result