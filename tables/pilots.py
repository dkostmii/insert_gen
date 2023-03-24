from pypika import Query, Table
from faker import Faker
from datetime import date
import re

def pilots(count: int):
    Faker.seed(123)

    faker = Faker()
    table = Table('Pilots')

    return "-- Pilots\n\n" + ";\n".join([
        str(Query.into(table)
            .columns('Id', 'First_Name', 'Last_Name', 'Phone', 'Email', 'Birth_Date', 'Employment_Date')
            .insert(
                i,
                faker.first_name(),
                faker.last_name(),
                '+' + re.sub(r'[\(\-x\)\.]', repl='', string=str(faker.phone_number()))[1:13],
                faker.email(),
                faker.date_between(date(1970, 1, 1), date(1997, 1, 1)),
                faker.date_between(date(2018, 1, 1), date(2023, 1, 1))
                ))
        for i in range(count)
    ]) + ";\n\n\n"
