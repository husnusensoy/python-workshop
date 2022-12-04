from filer import readers as r
from filer.excp import JsonFileNotFound

#r.read_json("data/a.json")

content = r.read_json("data/ab.json")

print(content)
#r.read_txt("data/aa.csv")

try:
    j = r.read_json("data/aa.json")
    t = r.read_txt("data/aa.csv")
except JsonFileNotFound as jfe:
    print(jfe)
    print(jfe.file_name)
    print(jfe.all_sims)
except TxtFileNotFound:
    ...