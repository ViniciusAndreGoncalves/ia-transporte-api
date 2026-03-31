from fastapi import APIRouter, Depends

from schemas.generate_schema import GenerateResponse
from use_cases.generate_use_cases import GenerateUseCases
from services.graphs import GraphService

from services.initalize import graphs

router = APIRouter()


@router.get("/gerar/kruskal")
def get_routes():
    usecase = GenerateUseCases()  # You can choose which graph to use
    return "Em Desenvolvimento..."

@router.get("/gerar/genetico")
def get_routes():
    usecase = GenerateUseCases()  # You can choose which graph to use
    return "Em Desenvolvimento..."