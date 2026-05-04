from fastapi import APIRouter, Depends

from src.use_cases.generate_use_cases import GenerateUseCases


router = APIRouter(prefix="/gerar", tags=["Geradores"])
"""Essas rotas ficam responsáveis pela geração da rota de ferrovia pelo Kruskal e Genético."""

@router.get("/kruskal")
def generate_krukal():
    """"Run Kruskal algorithm to generate Trail graph"""
    usecase = GenerateUseCases()
    result = usecase.generate_kruskal()

    return result


@router.get("/genetico")
def generate_genetico(population_size:int= 100, mutation_rate:float= 0.08, crossover_rate:float= 0.88, generations:int= 200):
    """Run Genetic algorithm to generate Trail graph"""
    usecase = GenerateUseCases()
    result = usecase.generate_genetic(population_size, mutation_rate, crossover_rate, generations)

    return result