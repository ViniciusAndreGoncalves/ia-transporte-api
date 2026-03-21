from fastapi import APIRouter, Depends

from schemas.generate_schema import GenerateResponse
from use_cases.generate_use_cases import GenerateUseCases
from services.graphs import GraphService

from services.initalize import graphs

router = APIRouter()


@router.get("", response_model=GenerateResponse)
def get_routes():
    usecase = GenerateUseCases(graphs.GRAPH1)  # You can choose which graph to use
    return "Em Desenvolvimento..."