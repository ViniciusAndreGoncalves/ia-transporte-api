from fastapi import APIRouter, Depends

from src.use_cases.generate_use_cases import GenerateUseCases


router = APIRouter(prefix="/gerar", tags=["Geradores"])

@router.get("/kruskal")
def generate_krukal():
    usecase = GenerateUseCases()
    result = usecase.generate_kruskal()

    return result


@router.get("/genetico")
def generate_genetico(population_size:int= 100, mutation_rate:float= 0.08, crossover_rate:float= 0.88, generations:int= 200):
    usecase = GenerateUseCases()
    result = usecase.generate_genetic(population_size, mutation_rate, crossover_rate, generations)
    return result