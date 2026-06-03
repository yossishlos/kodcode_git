from fastapi import FastAPI  # type: ignore[import]
from utils import io

app = FastAPI()

@app.get("/soldiers")
def get_soldiers():
    return io.get_soldiers()

@app.get("/soldiers/{id}")
def get_soldier_by_id(id: int):
    return io.get_soldier_by_id(id)

@app.post("/soldiers")
def add_soldier(new_soldier: dict):
    return io.add_soldier(new_soldier)

@app.put("/soldiers/{id}")
def update_soldier(id: int, new_data: dict):
    return io.update_soldier(id, new_data)