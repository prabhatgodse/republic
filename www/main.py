import sqlite3
from DataDumping import *
from SearchCongress import *
from server import start_server

sqlite3_connection = sqlite3.connect('../database/republic.db')

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

    # csearch = CongressSearch(sqlite3_connection)
    # res = csearch.search([CONGRESS_COLUMNS.FULL_NAME], ['ScottGarrett'], 'congress')
    # res = csearch.search_by_state('NY', 'sen')

    # print res
    start_server()

    sqlite3_connection.close()