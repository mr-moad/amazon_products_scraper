import sqlite3

con = sqlite3.connect('data.db')
if con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS products
        (ID INTEGER PRIMARY KEY    AUTOINCREMENT,
        title           TEXT    NOT NULL,
        price           TEXT    ,
        description           TEXT    NOT NULL,
        manufacturer           TEXT   ,
        images           TEXT    NOT NULL,
        link           TEXT    NOT NULL,
        category           TEXT    NOT NULL,
        model           TEXT    )
        ;''')
    cur.execute('''CREATE TABLE IF NOT EXISTS downloads
            (ID INTEGER PRIMARY KEY    AUTOINCREMENT,
            path           TEXT    NOT NULL,
            link           TEXT    )
            ;''')
    con.commit()
    con.close()