from pypika import Query, Table
from faker import Faker

def airports(count: int):
    Faker.seed(123)

    faker = Faker()
    table = Table('Airports')

    return "-- Airports\n\n" + ";\n".join([
        str(Query.into(table).columns('Id', 'Country', 'City').insert(i, faker.country(), faker.city()))
        for i in range(count)
    ]) + ";\n\n\n"
