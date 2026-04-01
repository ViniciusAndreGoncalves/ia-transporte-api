from fastapi import FastAPI
from src.services.graphs import GraphService
from src.services.algorithms import Kruskal, AStar, GeneticAlgorithm
from src.use_cases.generate_use_cases import GenerateUseCases
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

def main():
    pass
    # service = GraphService()
    # service.load("src/public/base_graph.json")

    # vortex, edges = service.create_graph()

    # kruskal_generate = Kruskal(vortex, edges)
    # kruskal_generate.run()
    # kruskal_generate.display()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/gerar/kruskal")
def get_kruskal():
    usecase = GenerateUseCases()
    result = usecase.generate_kruskal()

    return result

if __name__ == "__main__":
    main()