import sqlite3

import psycopg2
import pytest


def check_len_databases(table_name):
    dsl = {'dbname': 'movies_database', 'user': 'app', 'password': '123qwe', 'host': '127.0.0.1', 'port': 5432}
    with sqlite3.connect('../../db.sqlite') as sqlite_conn, psycopg2.connect(**dsl) as pg_conn:
        sqlite_conn.row_factory = sqlite3.Row
        sqlite_curs = sqlite_conn.cursor()
        sqlite_record = sqlite_curs.execute(f"SELECT * FROM {table_name}").fetchall()

        pg_curs = pg_conn.cursor()
        pg_curs.execute("SELECT version();")
        pg_curs.execute(f"select * from content.{table_name}")
        pg_record = pg_curs.fetchall()
        return len(sqlite_record) == len(pg_record)


def check_content_databases(table_name):
    dsl = {'dbname': 'movies_database', 'user': 'app', 'password': '123qwe', 'host': '127.0.0.1', 'port': 5432}
    with sqlite3.connect('../../db.sqlite') as sqlite_conn, psycopg2.connect(**dsl) as pg_conn:
        sqlite_conn.row_factory = sqlite3.Row
        sqlite_curs = sqlite_conn.cursor()
        sqlite_record = sqlite_curs.execute(f"SELECT * FROM {table_name}").fetchall()

        pg_curs = pg_conn.cursor()
        pg_curs.execute(f"select * from content.{table_name}")
        pg_record = pg_curs.fetchall()
        for i in range(len(pg_record)):
            if set(pg_record[i]) == set(tuple(sqlite_record[i])):
                return False
        return True

# тест на проверку длин таблиц
@pytest.mark.parametrize(
    'table', ('film_work',
              'genre',
              'genre_film_work',
              'person',
              'person_film_work')
)
def test_len(table: str):
    assert check_len_databases(table) is True


# тест на проверку содержимого таблиц
@pytest.mark.parametrize(
    'table', ('film_work',
              'genre',
              'genre_film_work',
              'person',
              'person_film_work')
)
def test_content(table: str):
    assert check_content_databases(table) is True

