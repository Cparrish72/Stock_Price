import sqlite3

def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def insert_stock_data(conn, stock_data):

    sql = ''' INSERT INTO stocks(date, ticker, open, high, low, close, volume)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, stock_data)
    conn.commit()
    return cur.lastrowid
