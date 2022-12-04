import requests
from prefect import flow, task


@flow
def my_favorite_fn() -> int:
    print("What is my fav number")

    return 42


@task
def call_api(url):
    res = requests.get(url)

    if res.status_code == 200:
        return res.json()
    else:
        return {}


@task
def parse_content(f: dict) -> str:
    return f.get("fact", "")


@flow
def scrape(url: str) -> str:
    fact = call_api(url)

    print(fact)
    fact_text = parse_content(fact)

    return fact_text


res = scrape("https://catfact.ninja/fact")

print(res)
