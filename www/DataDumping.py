import yaml
import sqlite3

def congress_search(db, param, value):
    cursor = db.cursor()
    sql = 'SELECT * FROM congress WHERE congress.{0} = ?'.format(param)
    cursor.execute(sql, (value,))

    sql_result = cursor.fetchall()
    return sql_result

def key_val(key, obj, default=''):
    return obj[key] if key in obj else default

def create_congress_table(db_conn):
    cursor = db_conn.cursor()
    createSql = """
        CREATE TABLE congress (
            userid INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name text,
            last_name text,
            full_name text,
            gender text,
            bioguide text,
            wikipedia text,
            birthday datetime
        );
    """

    result = cursor.execute(createSql)
    print 'Create congress table: ', result
    db_conn.commit()
    return result

def create_congress_terms_table(db_conn):
    cursor = db_conn.cursor()
    sql = """
        CREATE TABLE IF NOT EXISTS congressterms (
            uid INTEGER PRIMARY KEY AUTOINCREMENT,
            userid text,
            type text,
            start_date date,
            end_date date,
            state text,
            class text,
            party text,
            url text,
            address text,
            phone text,
            fax text,
            contact_form text,
            office text
        )
    """
    result = cursor.execute(sql)
    print 'Create congress terms table: ', result
    db_conn.commit()
    return result

def create_congress_social_media_table(db_conn):
    cursor = db_conn.cursor()

    # uid is the userid from congress table

    sql = """
        CREATE TABLE IF NOT EXISTS congress_social_media (
            uid TEXT PRIMARY KEY,
            twitter text,
            facebook text,
            youtube text,
            instagram text,
            facebook_id text,
            youtube_id text,
            twitter_id text
        );
    """
    cursor.execute(sql)
    db_conn.commit()

def insert_congress(congress, db_conn):
    cursor = db_conn.cursor()
    n = congress['name']
    first_name = n['first']
    middle_name = key_val('middle', n)
    last_name = n['last']
    gender = congress['bio']['gender']

    dat = congress['id']
    bioguide = key_val('bioguide', dat)
    wikipedia = key_val('wikipedia', dat)
    birthday = congress['bio']['birthday']
    full_name = first_name + middle_name + last_name

    sql = """
        INSERT INTO congress (
            first_name,
            last_name,
            full_name,
            gender,
            bioguide,
            wikipedia,
            birthday
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """

    cursor.execute(sql, (first_name, last_name, full_name, gender, bioguide, wikipedia, birthday))
    db_conn.commit()

def get_yaml_data(file_path):
    legisData = open(file_path, "r")

    legisYaml = yaml.load(legisData)
    print 'YAML load complete: ', len(legisYaml)
    return legisYaml

def create_congress_data(db_conn):
    fpath = "../data/congress-legislators-master/legislators-current.yaml"
    legisYaml = get_yaml_data(fpath)

    count = 0
    republican = 0
    for l in legisYaml:
        terms = l['terms']
        lastTerm = terms[-1]
        insert_congress(l, db_conn)
        if lastTerm['type'] == 'sen':
            name = l['name']
            count = count + 1

            if lastTerm['party'] == 'Republican':
                republican = republican + 1

    print 'Republican: ', republican

def create_congress_terms_data(db_conn):
    cursor = db_conn.cursor()
    fpath = "../data/congress-legislators-master/legislators-current.yaml"
    legislators = get_yaml_data(fpath)

    sql = """
        INSERT INTO congressterms (
            userid,
            type,
            start_date,
            end_date,
            state,
            class,
            party,
            url,
            address,
            phone,
            fax,
            contact_form,
            office
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    for l in legislators:
        terms = l['terms']
        name = l['name']

        n = l['name']
        first_name = n['first']
        middle_name = key_val('middle', n)
        last_name = n['last']

        userid = first_name + middle_name + last_name

        for t in terms:
            typ = key_val('type', t)
            start_date = key_val('start', t)
            end_date = key_val('end', t)
            state = key_val('state', t)
            cl = str(key_val('class', t))
            party = key_val('party', t)
            url = key_val('url', t)
            address = key_val('address', t)
            phone = key_val('phone', t)
            fax = key_val('fax', t)
            contact_form = key_val('contact_form', t)
            office = key_val('office', t)

            cursor.execute(sql, (
                userid,
                typ,
                start_date,
                end_date,
                state,
                cl,
                party,
                url,
                address,
                phone,
                fax,
                contact_form,
                office
            ))
            db_conn.commit()


def create_congress_social_media_data(db_conn):
    cursor = db_conn.cursor()

    fpath = "../data/congress-legislators-master/legislators-social-media.yaml"
    ydata = get_yaml_data(fpath)

    sql = """
        INSERT INTO congress_social_media (
            uid,
            twitter,
            facebook,
            youtube,
            instagram,
            facebook_id,
            youtube_id,
            twitter_id
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """

    for y in ydata:
        yid = key_val('id', y)
        bioguide = key_val('bioguide', yid)
        congress = congress_search(db_conn, 'bioguide', bioguide)
        if congress:
            social = key_val('social', y, 0)

            if not social:
                continue

            uid = congress[0][0]
            twitter = key_val('twitter', social)
            facebook = key_val('facebook', social)
            youtube = key_val('youtube', social)
            instagram = key_val('instagram', social)
            facebook_id = key_val('facebook_id', social)
            youtube_id = key_val('youtube_id', social)
            twitter_id = str(key_val('twitter_id', social))

            cursor.execute(sql, (
                uid,
                twitter,
                facebook,
                youtube,
                instagram,
                facebook_id,
                youtube_id,
                twitter_id
            ))
            db_conn.commit()




def search_congressmen(name, db):
    sql = """
         select * from congress
         INNER JOIN congressterms
         ON congress.full_name = congressterms.userid
         WHERE congress.full_name = ?;
    """
    cursor = db.cursor()
    cursor.execute(sql, (name,))

    val = cursor.fetchall()
    print 'Search complete: ', val
    return val

def search_congress_location(state, type, db):
    sql = """
        SELECT userid, state, party, type, MAX(start_date)
        FROM congressterms
        WHERE state=? AND type=?
        GROUP BY userid;
    """
    cursor = db.cursor()
    cursor.execute(sql, (state, type))
    val = cursor.fetchall()

    print 'Congress by location= '
    for v in val:
        print v