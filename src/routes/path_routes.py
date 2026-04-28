from fastapi import APIRouter
from src.use_cases.path_use_cases import PathUseCases

# Classe feita para retornar ao front a resposta(em formato de lista) do caminho escolhido

router = APIRouter(prefix="/rota", tags=["Caminhos"])

path_use_case = PathUseCases()

@router.get("/")
def get_path(start:str, end:str):

    return path_use_case.find_path(start, end)

@router.get("/kruskal")
def get_kruskal_path(start:str, end:str):

    return path_use_case.find_path_kruskal(start, end)

@router.get("/genetico")
def get_genetic_path(start:str, end:str):

    return path_use_case.find_path_genetico(start, end)