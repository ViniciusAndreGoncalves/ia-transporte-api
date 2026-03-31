from fastapi import APIRouter, Depends
from use_cases.graph_use_cases import GraphUseCase


router = APIRouter()

graph_use_case = GraphUseCase()

@router.get("/grafo")
def get_graph():
    graph_use_case.get_graph()

    return "Em Desenvolvimento..."

@router.get("/grafo/kruskal")
def get_graph():
    graph_use_case.get_graph_kruskal()

    return "Em Desenvolvimento..."

@router.get("/grafo/genetico")
def get_graph():
    graph_use_case.get_graph_genetico()
    
    return "Em Desenvolvimento..."