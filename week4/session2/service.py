import json
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#store = PGStore()
#store = MongoStore()
#store = JsonStore()


class Car(BaseModel):
    brand: str
    model: str
    year: Union[None, int] = 2022
    door_count: int
    price: Union[None, float] = -1.


@app.get("/")
def hello() -> dict:
    """My first service endpoint  saying hello"""
    return {"message": "Hello World"}


@app.get("/{name}")
def hello_to_name(name: str, year: int = 2022) -> dict:
    """My first service endpoint  saying hello"""

    if year == 2022:
        return {"message": f"Hello {name.title()}!!!"}
    elif year < 2022:
        return {"message": f"Hello {name.title()}!!! (back in history)"}
    else:
        return {"message": f"Hello {name.title()}!!! (back to the future)"}


def in_db(car:Car) -> bool:

    """returns true if car is in db false o/w"""

    with open("database/cars.json") as fp:
        j = json.load(fp)

    #return (car.brand, car.model) in j

    return f"{car.brand}:{car.model}" in j

def fetch(brand:str, model:str) -> Car:
    with open("database/cars.json") as fp:
        j = json.load(fp)

    c = j[f"{brand}:{model}"]

    #return Car(brand=car['brand'], model=car['model'], year=car['year'], door_count=car['door_count'], price=car['price'])
    return Car(**c)


def store(car:Car) -> Car:
    with open("database/cars.json") as fp:
        j = json.load(fp)

    j[f"{car.brand}:{car.model}"] = car.dict()

    with open("database/cars.json","w") as fp:
        json.dump(j, fp)

    return car  

@app.post("/cars/")
def create_car(car: Car):
    if not in_db(car):
        return store(car)
    else:
        return fetch(car.brand, car.model)


@app.get("/cars/{brand}/{model}")
def get_car(brand:str, model:str):
    return fetch(brand,model)
    
