from fastapi import APIRouter, Depends
from use_cases.path_use_cases import PathUseCases


router = APIRouter()

path_use_case = PathUseCases()

@router.get("/rota")
def get_graph(response):
    start = response.start
    end = response.end

    path = path_use_case.find_path()

    return "Em Desenvolvimento..."

@router.get("/rota/kruskal")
def get_graph(response):
    start = response.start
    end = response.end

    path = path_use_case.find_path_kruskal()

    return "Em Desenvolvimento..."

@router.get("/rota/genetico")
def get_graph(response):
    start = response.start
    end = response.end

    path = path_use_case.find_path_genetico()

    return "Em Desenvolvimento..."