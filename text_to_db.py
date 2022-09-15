import sqlite3
import ast

def create_db(con):
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS links
        (ID INTEGER PRIMARY KEY    AUTOINCREMENT,
        link           TEXT    NOT NULL,
        category           TEXT    NOT NULL,
        in_use           TEXT    NOT NULL,
        used           TEXT    )
        ;''')
    con.commit()


def add_record(data):
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute(
                f"INSERT INTO links (link, category, in_use, used) VALUES (?,?,?,?)",
        (data['link'],data["category"], "False", "False")
                )
    con.commit()


def get_record(con, limit = 1):
    con = sqlite3.connect("data.db")
    con.row_factory = sqlite3.Row
    cur= con.cursor()
    res = cur.execute(f"SELECT * FROM links WHERE in_use = 'False' AND used = 'False' LIMIT {limit}")
    data = res.fetchall()
    con.commit()
    return data



def set_record_in_use(con, record_id):
    con.row_factory = sqlite3.Row
    cur= con.cursor()
    cur.execute(f"UPDATE links SET in_use = 'True' WHERE ID = '{record_id}'")
    con.commit()


def set_record_used(con, record_id):
    con.row_factory = sqlite3.Row
    cur= con.cursor()
    cur.execute(f"UPDATE links SET used = 'True' WHERE ID = '{record_id}'")
    con.commit()


def set_all_records_unsued(con):
    con.row_factory = sqlite3.Row
    cur= con.cursor()
    cur.execute(f"UPDATE links SET in_use = 'False'")
    con.commit()


if __name__ == "__main__":
    create_db()
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    with open("product_links.txt", "r+") as p_links:
        lines = p_links.read().splitlines()
    for line in lines:
        try:
            object_data = ast.literal_eval(line)
            cur.execute(
                f"INSERT INTO links (link, category, in_use, used) VALUES (?,?,?,?)",
                (object_data['link'], object_data["category"], "False", "False")
            )
        except:
            pass
    con.commit()
    con.close()
        # add_record(object_data)
    # create_db()
