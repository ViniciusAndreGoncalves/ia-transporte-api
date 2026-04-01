from fastapi import APIRouter, Depends, FastAPI

from src.use_cases.generate_use_cases import GenerateUseCases
from src.services.graphs import GraphService

from src.services.initalize import graphs

router = APIRouter(prefix="/gerar", tags=["Geradores"], dependencies=[Depends(graphs)])

@router.get("/kruskal")
def get_routes():
    usecase = GenerateUseCases()
    mst = usecase.generate_kruskal()

    return mst


@router.get("/genetico")
def get_routes():
    usecase = GenerateUseCases()
    return "Em Desenvolvimento..."