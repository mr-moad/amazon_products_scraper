import sqlite3, os, shutil
import requests

from utils import save_data


def save_image():
    con = sqlite3.connect("data.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    res = cur.execute("SELECT * FROM downloads")
    data = res.fetchall()
    con.commit()
    con.close()
    return data


def walo():
    data = save_image()
    for d in data:
        r = requests.get(d["link"], stream=True)
        if r.status_code == 200:
            with open(d["path"], 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)




def fix_xls():
    con = sqlite3.connect("data.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    res = cur.execute("SELECT * FROM products")
    data = res.fetchall()
    con.commit()
    con.close()
    new_data = []
    for d in data:
        new_data.append({
            "title": d["title"],
            "description": d["description"],
            "manufacturer": d["manufacturer"],
            "price": d["price"],
            "images": d["images"],
            "model": d["model"],
            "link": d["link"],
            "category": d["category"]
        })
    counter = 0
    while new_data:
        save_data(new_data[:65000],counter)
        new_data = new_data[65000:]
        counter += 1
fix_xls()