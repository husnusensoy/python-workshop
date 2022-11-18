from .base import BaseStore

"""For more details please refer to 
    https://www.sqlalchemy.org/
"""


class RelationalStore(BaseStore):
    def in_db(self, car: Car):
        ...

    def create(self, car: Car):
        ...

    def get(self, car: Car):
        ...
