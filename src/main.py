from fastapi import FastAPI
from src.routes import path_routes, generate_routes, graph_routes
from fastapi.middleware.cors import CORSMiddleware
from src.test import run

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/test")
def run_test():
    run()

app.include_router(path_routes.router)
app.include_router(generate_routes.router)
app.include_router(graph_routes.router)

