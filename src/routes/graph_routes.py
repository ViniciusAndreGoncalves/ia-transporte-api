from fastapi import APIRouter, Depends
from src.use_cases.graph_use_cases import GraphUseCase


router = APIRouter(prefix="/grafo", tags=["Grafos"])

graph_use_case = GraphUseCase()

@router.get("/")
def get_graph():
    result = graph_use_case.get_graph()

    return result

@router.get("/kruskal")
def get_graph_kruskal():
    result = graph_use_case.get_graph_kruskal()

    return result

@router.get("/genetico")
def get_graph_genetico():
    result = graph_use_case.get_graph_genetico()
    
    return result