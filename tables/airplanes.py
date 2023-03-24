from random import randint, seed
from pypika import Query, Table

def next_capacity():
    return randint(6, 35) * 5

def airplanes(count: int):
    seed(123)
    table = Table('Airplanes')
    return "-- Airplanes\n\n" + ";\n".join([
        str(Query.into(table).columns('Id', 'Capacity').insert(i, next_capacity()))
        for i in range(count)]) + ";\n\n\n"
