import jinja2
from jinja2 import Environment, FileSystemLoader

envi = jinja2.Environment()


template = envi.from_string("Hello, {{ name }} !")

print(template.render(name="Hüsnü"))


envi2 = Environment(loader=FileSystemLoader("templates/"))

template = envi2.get_template("message.txt.j2")

# students = [
#     dict(name="Joe", score=100),
#     dict(name="Bob", score=87),
#     dict(name="Jane", score=92),
# ]

import pandas as pd

students = pd.read_csv("data/students.csv").to_dict("records")

max_score = 120
test_name = "Python Templating Challange"


for s in students:
    content = template.render(s, max_score=max_score, test_name=test_name)

    #print(content)

template = envi2.get_template("message-batch.txt.j2")

content = template.render(students=students, max_score=max_score, test_name=test_name)

print(content)