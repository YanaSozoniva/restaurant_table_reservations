from datetime import date, time
import pytest

from reservation.factories import ReservationFactory, TableFactory
from reservation.services import get_free_tables


@pytest.mark.django_db
def test_get_free_tables():
    tables = TableFactory.create_batch(10)
    # print(f"Created {len(tables)} tables")

    for i, table in enumerate(tables[:5]):
        reservation = ReservationFactory.create(
            table=table,
            time_reservation=time(17, 10)
        )
        # print(f"{reservation.table.pk} {reservation.time_reservation} кол-во часов брони {reservation.count_hours} кол-во яеловек {reservation.count_people}")

    for i, table in enumerate(tables[6:9]):
        reservation = ReservationFactory.create(
            table=table,
            time_reservation=time(16, 10)
        )
        # print(
        #     f"{reservation.table.pk} {reservation.time_reservation} кол-во часов брони {reservation.count_hours} кол-во яеловек {reservation.count_people}")
    available_tables = get_free_tables(
        date_reservation=date(2025, 9, 17),
        time_reservation=time(16, 10)
    )

    print(f"Available tables: {len(available_tables)}")
    for table in available_tables:
        print(f"Table {table.id} is available")

    assert len(available_tables) == 2
