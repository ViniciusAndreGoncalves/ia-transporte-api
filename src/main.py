from fastapi import FastAPI
from services.graphs import GraphService
from services.algorithms import Kruskal, AStar, GeneticAlgorithm

app = FastAPI()

def main():
    service = GraphService()
    service.load("src/public/base_graph.json")

    vortex, edges = service.create_graph()

    kruskal_generate = Kruskal(vortex, edges)
    kruskal_generate.run()
    kruskal_generate.display()

if __name__ == "__main__":
    main()