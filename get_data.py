import os.path
import sqlite3
import time
from selenium import webdriver
import ast
import threading

from text_to_db import get_record, set_all_records_unsued, set_record_used, set_record_in_use
from utils import save_data, download_image, query_products
all_products = []
BASE_DIR = './recomendation'



def get_data(con, driver, counter_product,link,category, products_id):
    product_images = []
    time.sleep(1)
    number = None
    manufacturer = None
    title = None
    price = None
    description = None
    try:
        title = driver.execute_script(open("scripts/utils/title.js").read())
    except Exception as e:
        print(e)
    try:
        number = driver.execute_script(open("scripts/utils/model.js").read())
    except:
        pass

    try:
        manufacturer = driver.execute_script(open("scripts/utils/manufacturer.js").read())
    except Exception as e:
        pass

    try:
        price = driver.execute_script(open("scripts/utils/price.js").read())
    except:
        pass

    try:
        description = driver.execute_script(open("scripts/utils/description.js").read())
    except:
        try:
            description = driver.execute_script("return document.querySelector('#featurebullets_feature_div').innerText")
        except:
            pass

    try:
        images = driver.execute_script(open("scripts/utils/show_images.js").read())
        for image in images:
            product_images.append(download_image(con=con,product_count=counter_product, image=image))
    except:
        pass
    if not title and not product_images and not description and not price:
        set_record_used(con, products_id)
        return True
    elif not description:
        set_record_used(con, products_id)
        return True

    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO products (title, description, manufacturer, price, images, model, link, category) VALUES (?, ?,?,?,?,?,?,?)",
        (title, description, manufacturer, price, ",".join(product_images), number, link,category))
    con.commit()
    save_data([{
        "description": title,
        "manufacturer": manufacturer,
        "price": price,
        "images": ",".join(product_images),
        "model": number,
        "link": link,
        "category": category
    }])
    set_record_used(con, products_id)


def start_scraping(con, all_data,count):
    options = webdriver.ChromeOptions()

    options.add_argument('--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data')

    options.add_argument('--profile-directory=Default')

    driver = webdriver.Chrome(options=options, executable_path="a.exe")
    # driver = webdriver.Chrome(executable_path="a.exe")
    driver.minimize_window()
    for data in all_data:
        link = data["link"]
        driver.execute_script(f'window.open("{link}","_blank");')
    time.sleep(0.3)
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    time.sleep(0.3)
    local_count = count
    for window in driver.window_handles:
        driver.switch_to.window(window)
        get_data(con, driver, local_count,all_data[-1]["link"],all_data[-1]["category"], all_data[-1]["ID"])
        local_count += 1
        all_data = all_data[:-1]
    driver.quit()


def scrape_data():
    con = sqlite3.connect("data.db")
    set_all_records_unsued(con)
    records = get_record(con, 8)
    counter_product = len(next(os.walk(BASE_DIR))[1])
    while os.path.exists(f"recomendation/{counter_product}"):
        counter_product += 1
    start_scraping(con, records,counter_product)
    con.close()
    counter_product += 1



if __name__ == "__main__":
    while True:
        scrape_data()