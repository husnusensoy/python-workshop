import json
import time
from dataclasses import dataclass
from typing import Dict, Union

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


def all(bools: List[bool]) -> bool:

    for b in bools:
        if not b:
            return False
    return True
    

def any(bools: List[bool]) -> bool:

    for b in bools:
        if  b:
            return True

    return False

class Product(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


class MetaInfo(BaseModel):
    elapsed: float
    file_name: str


class ProductResponse(BaseModel):
    name: str
    meta: MetaInfo


app = FastAPI()


@app.get("/")
def root() -> Dict[str, str]:
    """This is my first handler/function/service"""

    return dict(message="Hello World")


@app.get("/hello/{name}")
def hello_world(name: str) -> Dict[str, str]:
    return dict(message=f"Hello {name} !")


@app.get("/hello/{company}/{year}")
def hello_company(company: str, year: int) -> Dict[str, str]:
    return dict(message=f"{company} sends you greetings in {year} !")


@app.post("/products/")
def create_product(item: Product):
    t0 = time.time()

    with open("products.json") as fp:
        products = json.load(fp)

    if any([prod["name"] == item.name for prod in products]):
        raise HTTPException(
            status_code=422,
            detail=f"Product {item.name} is already available in database",
        )
    else:
        products.append({"name": item.name, "price": item.price})

        with open("products.json", "w") as wp:
            json.dump(products, wp)

    t1 = time.time()

    return ProductResponse(
        name=item.name, meta=MetaInfo(file_name="products.json", elapsed=t1 - t0)
    )


# def entrypoint():
#     response = root()


#     print(response)

# if __name__ == "__main__":
#     entrypoint()
