import psycopg2


def db_connector(username, password,database,  host="127.0.0.1", port="5432"):
    try:
        connection = psycopg2.connect(user = username,
                                    password = password,
                                    host = host,
                                    port = port,
                                    database = database)
        cursor = connection.cursor()
        dsn_params = connection.get_dsn_parameters()
        print(f"Connected to '{dsn_params['dbname']}' as '{dsn_params['user']}'\n\n ")

        return cursor, connection

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)


def db_handler(connector_cursor, query):
    try:
        connector_cursor.execute(query)
        records = connector_cursor.fetchall()
        return records
    except:
        print("Fetching failed.")


def db_committer(connector_cursor, connection, query):
    # try:
    connector_cursor.execute(query)
    connection.commit()
    # except:
    #     print("Committing failed.")




my_cursor, my_connection = db_connector(username="ali", password="ali", database="bootcamp")

table_account_query = """CREATE TABLE IF NOT EXISTS accounts (
                        userid serial PRIMARY KEY,
                        username VARCHAR ( 50 ) UNIQUE NOT NULL,
                        password VARCHAR ( 50 ) NOT NULL,
                        email VARCHAR ( 255 ) UNIQUE,
                        created_on TIMESTAMP,
                        last_login TIMESTAMP
                        );"""

table_profile_query = """CREATE TABLE IF NOT EXISTS profile (
                        profileid SERIAL PRIMARY KEY,
                        userid INT NOT NULL,
                        grantdate TIMESTAMP,
                        FOREIGN KEY (userid)
                            REFERENCES accounts (userid)
                        );"""

db_committer(my_cursor, my_connection, table_account_query)
db_committer(my_cursor, my_connection, table_profile_query)

# query = """INSERT INTO profile (userid, grantdate) 
#                     VALUES (2, '2020-5-3')
#                     ;"""

# query = """
#         ALTER TABLE profile DROP CONSTRAINT profile_userid_fkey;
#         """

# query = """
#         ALTER TABLE profile ALTER COLUMN userid TYPE VARCHAR(50) ;
#         """

# query = """
#         UPDATE profile 
#         SET userid = 'ali';
#         """

# query = """
#         ALTER TABLE profile ADD CONSTRAINT userid_fkey FOREIGN KEY (userid) REFERENCES accounts(username);
#         """

query = """
        insert into profile(userid) values('bala');
"""
db_committer(my_cursor, my_connection, query)

query = "SELECT * FROM accounts limit 10;"
print(db_handler(my_cursor, query))

my_cursor.close()
my_connection.close()
print("Connection closed successfully.")