from fastapi import FastAPI
from pydantic import BaseModel

from enum import Enum


class CarModels(str, Enum):
    miura = "miura"
    diablo = "diablo"
    huracan = "huracan"

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World, from FastAPI"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/items/")
async def create_item(item: Item):
    
    return item

@app.get("/models/{car_name}")
async def get_car(car_name: CarModels):
    if car_name is CarModels.diablo:
        return{"car_name": car_name, "message": "Legendary 90's super car"}
    
    if car_name is CarModels.miura:
        return{"car_name": car_name, "message": "Legendary late 60's and early 70's super car"}
    
    # if car_name.value == "miura":
    #     return{"car_name": car_name, "message": "Legendary late 60's and early 70's super car"}
    
    return {"car_name": car_name, "message": "That's the new generatiom"}