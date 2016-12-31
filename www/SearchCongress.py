import sqlite3

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

class CONGRESS_TERMS_COLUMNS:
    UID = 'uid'
    USERID = 'userid'
    TYPE = 'type'
    START_DATE = 'start_date'
    END_DATE = 'end_date'
    STATE = 'state'
    CLASS = 'class'
    PARTY = 'party'
    URL = 'url'
    ADDRESS = 'address'
    PHONE = 'phone'
    FAX = 'fax'
    CONTACT_FORM = 'contact_form'
    OFFICE = 'office'

congress_terms_column_order = [
    CONGRESS_TERMS_COLUMNS.UID,
    CONGRESS_TERMS_COLUMNS.USERID,
    CONGRESS_TERMS_COLUMNS.TYPE,
    CONGRESS_TERMS_COLUMNS.START_DATE,
    CONGRESS_TERMS_COLUMNS.END_DATE,
    CONGRESS_TERMS_COLUMNS.STATE,
    CONGRESS_TERMS_COLUMNS.CLASS,
    CONGRESS_TERMS_COLUMNS.PARTY,
    CONGRESS_TERMS_COLUMNS.URL,
    CONGRESS_TERMS_COLUMNS.ADDRESS,
    CONGRESS_TERMS_COLUMNS.PHONE,
    CONGRESS_TERMS_COLUMNS.FAX,
    CONGRESS_TERMS_COLUMNS.CONTACT_FORM,
    CONGRESS_TERMS_COLUMNS.OFFICE
]

class CONGRES_SOCIAL_MEDIA_COLUMNS:
    UID = 'uid'
    TWITTER = 'twitter'
    FACEBOOK = 'facebook'
    YOUTUBE = 'youtube'
    INSTAGRAM = 'instagram'
    FACEBOOK_ID = 'facebook_id'
    YOUTUBE_ID = 'youtube_id'
    TWITTER_ID = 'twitter_id'

congress_social_media_coulmn_order = [
    CONGRES_SOCIAL_MEDIA_COLUMNS.UID,
    CONGRES_SOCIAL_MEDIA_COLUMNS.TWITTER,
    CONGRES_SOCIAL_MEDIA_COLUMNS.FACEBOOK,
    CONGRES_SOCIAL_MEDIA_COLUMNS.YOUTUBE,
    CONGRES_SOCIAL_MEDIA_COLUMNS.INSTAGRAM,
    CONGRES_SOCIAL_MEDIA_COLUMNS.FACEBOOK_ID,
    CONGRES_SOCIAL_MEDIA_COLUMNS.YOUTUBE_ID,
    CONGRES_SOCIAL_MEDIA_COLUMNS.TWITTER_ID
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

    def search_congress_social_media(self, userid):
        sql = 'SELECT * FROM congress_social_media WHERE uid = ?'
        cursor = self.db.cursor()
        cursor.execute(sql, (userid,))

        return cursor.fetchall()

    def jsonify_items(self, items, columns):
        jres = {}
        if len(items) != len(columns):
            print 'ERROR: Input array size incorrect {0} != {1}'.format(len(items), len(columns))
            return {}

        for idx, each in enumerate(items):
            jres[columns[idx]] = each

        return jres

    def jsonify_congress_and_terms(self, items):
        columns = congress_columns_order + congress_terms_column_order
        return self.jsonify_items(items, columns)

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

        res = cursor.fetchall()

        json_res = []
        for r in res:
            # A bit hacky but remove last item since it's MAX(start_date) from SQL
            rmod = list(r)
            userid = str(rmod[0])
            # rmod.append(r)
            # rmod = list(rmod[0])
            rmod.pop()
            each = self.jsonify_congress_and_terms(rmod)

            smedia = self.search_congress_social_media(userid)
            smedia = list(smedia[0])
            smedia = smedia[1:]
            smedia_json = self.jsonify_items(smedia, congress_social_media_coulmn_order[1:])
            each['social_media'] = smedia_json
            json_res.append(each)

        return json_res