from faker import Faker

from tables.airplanes import airplanes
from tables.airports import airports
from tables.pilots import pilots
from tables.planned_flights import planned_flights
from tables.planned_flights_pilots import planned_flights_pilots
from delete import delete

from contextlib import redirect_stdout

from os import mkdir
from os.path import exists


def main():
    airplanes_count = 10
    airports_count = 10
    pilots_count = 50
    planned_flights_count = 10
    planned_flights_pilots_count = 10

    print('Generating generated/insert.sql file...')

    if not exists('generated'):
        print('Creating generated/ dir...')
        mkdir('generated')

    with open('generated/insert.sql', 'w') as f:
        with redirect_stdout(f):
            print(delete())
            print(airplanes(airplanes_count), end='')
            print(airports(airports_count), end='')
            print(pilots(pilots_count), end='')
            print(planned_flights(planned_flights_count, airplanes_count, airports_count), end='')
            print(planned_flights_pilots(planned_flights_pilots_count, planned_flights_count, pilots_count))

    print("Done.")


if __name__ == "__main__":
    main()
