import pandas as pd
from faker import Faker
from tqdm import tqdm, trange

faker = Faker()

d = {
    "name":[],
    "color":[],
    "cc":[]
}


for _ in trange(100_000):
    d['name'].append(faker.name())
    d['color'].append(faker.color_name())
    d['cc'].append(faker.credit_card_number())

df = pd.DataFrame(d)

#print(df)

df.to_csv("data/sample.csv", index=False,header=False)


    

