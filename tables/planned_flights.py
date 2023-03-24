from pypika import Query, Table
from faker import Faker
from random import seed, randint, sample
from datetime import date, timedelta, datetime


def next_airport_indices(airports_count: int):
    s = sample(range(airports_count), 2)
    return s[0], s[1]


def next_timedelta():
    return timedelta(minutes=randint(45, 600))


def format_datetime(dt: datetime):
    return f'{dt.year}-{str(dt.month).zfill(2)}-{str(dt.day).zfill(2)} {str(dt.hour).zfill(2)}:{str(dt.minute).zfill(2)}:{str(dt.second).zfill(2)}'


def planned_flights(count: int, airplanes_count: int, airports_count: int):
    seed(123)
    Faker.seed(123)

    faker = Faker()
    table = Table('Planned_Flights')

    queryData = []

    for i in range(count):
        id = i
        departure_at = faker.date_time_between_dates(date(2023, 4, 30), date(2023, 12, 31))
        arrival_at = departure_at + next_timedelta()
        departure_at = format_datetime(departure_at)
        arrival_at = format_datetime(arrival_at)
        airplanes_id = randint(0, airplanes_count - 1)
        airports_departure_id, airports_destination_id = next_airport_indices(airplanes_count)

        queryData.append([id, departure_at, arrival_at, airplanes_id, airports_departure_id, airports_destination_id])


    return "--Planned_Flights\n\n" + ";\n".join([
        str(Query
            .into(table)
            .columns('Id', 'Departure_At', 'Arrival_At', 'Airplanes_Id', 'Airports_Departure_Id', 'Airports_Destination_Id')
            .insert(data[0], data[1], data[2], data[3], data[4], data[5]))
        for data in queryData
    ]) + ";\n\n\n"
