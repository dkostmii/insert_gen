from random import randint, seed
from pypika import Query, Table


def next_planned_flights_id(planned_flights_count: int):
    return randint(0, planned_flights_count - 1)


def next_pilots_id(pilots_count: int):
    return randint(0, pilots_count)


def planned_flights_pilots(count: int, planned_flights_count: int, pilots_count: int):
    seed(123)

    table = Table("Planned_Flights_Pilots")

    return "-- Planned_Flights_Pilots\n\n" + ";\n".join([
        str(Query
            .into(table)
            .columns('Id', 'Planned_Flights_Id', 'Pilots_Id')
            .insert(i, next_planned_flights_id(planned_flights_count), next_pilots_id(pilots_count)))
        for i in range(count)
    ]) + ";\n\n\n"
    