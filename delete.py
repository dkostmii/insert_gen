from pypika import Query, Table

def delete():
    tables = [
        Table('Planned_Flights_Pilots'),
        Table('Planned_Flights'),
        Table('Pilots'),
        Table('Airports'),
        Table('Airplanes')
    ]

    return "-- Clear tables\n\n" + ";\n".join([
        str(Query.from_(table).delete())
        for table in tables
    ]) + ";\n\n"
