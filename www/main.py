import sqlite3
from DataDumping import *

sqlite3_connection = sqlite3.connect('../database/republic.db')

class SQL_TYPES:
    INT = 1
    STRING = 2
    DATETIME = 3

class CONGRESS_COLUMNS:
    USERID = 'userid'
    FIRST_NAME = 'first_name'
    LAST_NAME = 'last_name'
    FULL_NAME = 'full_name'
    GENDER = 'gender'
    BIOGUIDE = 'bioguide'
    WIKIPEDIA = 'wikipedia'
    BIRTHDAY = 'birthday'

congress_column_type = {
    'userid': SQL_TYPES.INT,
    'first_nam': SQL_TYPES.STRING,
    'last_nam': SQL_TYPES.STRING,
    'full_name': SQL_TYPES.STRING,
    'gender': SQL_TYPES.STRING,
    'bioguide': SQL_TYPES.STRING,
    'wikipedia': SQL_TYPES.STRING,
    'birthday': SQL_TYPES.DATETIME
}

congress_columns_order = [
    CONGRESS_COLUMNS.USERID,
    CONGRESS_COLUMNS.FIRST_NAME,
    CONGRESS_COLUMNS.LAST_NAME,
    CONGRESS_COLUMNS.FULL_NAME,
    CONGRESS_COLUMNS.GENDER,
    CONGRESS_COLUMNS.BIOGUIDE,
    CONGRESS_COLUMNS.WIKIPEDIA,
    CONGRESS_COLUMNS.BIRTHDAY
]

class CongressSearch:
    def __init__(self, db):
        self.db = db

    def search(self, params, values, table):
        if len(params) != len(values):
            print 'ERROR: number of params and values must be same'
        sql = 'SELECT * FROM {0} WHERE '.format(table)
        for p in params:
            sql = sql + ' ' + p + ' LIKE ? '
            if p != params[-1]:
                sql = sql + ' AND '

        values[:] = ['%' + v + '%' for v in values]

        print sql
        cursor = self.db.cursor()
        cursor.execute(sql, values)
        res = cursor.fetchall()
        return res

    def search_by_state(self, state, type):
        sql = """
            SELECT *
            FROM congress
            INNER JOIN (
                    SELECT *, MAX(start_date)
                    FROM congressterms
                    WHERE congressterms.state = ? AND congressterms.type = ?
                    GROUP BY userid
            ) AS ct
            ON ct.userid = congress.full_name;
        """
        cursor = self.db.cursor()
        cursor.execute(sql, (state, type))
        return cursor.fetchall()


if __name__ == '__main__':
    # create_congress_table(sqlite3_connection)
    # create_congress_data(sqlite3_connection)

    # create_congress_terms_table(sqlite3_connection)
    # create_congress_terms_data(sqlite3_connection)

    # create_congress_social_media_table(sqlite3_connection)
    # create_congress_social_media_data(sqlite3_connection)

    #Open the House of Rep HTML file

    # results = search_congressmen('PaulD.Ryan', sqlite3_connection)
    # search_congress_location('FL', 'sen', sqlite3_connection)
    # for cc in parser.congressList:
    #     print 'C name: ', cc.name

    csearch = CongressSearch(sqlite3_connection)
    # res = csearch.search([CONGRESS_COLUMNS.FULL_NAME], ['ScottGarrett'], 'congress')
    res = csearch.search_by_state('NY', 'sen')

    for r in res:
        uid = str(r[0])
        social = csearch.search(['uid'], [uid], 'congress_social_media')
        print social
    sqlite3_connection.close()