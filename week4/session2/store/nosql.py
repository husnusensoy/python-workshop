from .base import BaseStore


class CassandraStore:
    def in_db(self, car:Car):
        ...

    def create(self, car:Car):
        ...

    def get(self, car:Car):
        ...