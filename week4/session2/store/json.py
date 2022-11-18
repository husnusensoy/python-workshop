from .base import BaseStore


class JsonStore(BaseStore):
    def in_db(self, car:Car):
        ...

    def create(self, car:Car):
        ...

    def get(self, car:Car):
        ...