import time
import threading
from selenium import webdriver
import ast


class StartScraping:
    def __init__(self, driver, link):
        self.driver = driver
        self.link = link

    def get_link(self):
        while True:
            try:
                self.driver.get(self.link)
                break
            except:
                pass

    def get_products(self):
        try:
            d = self.driver.execute_script(open("scripts/amazon-products.js").read())
            if not d:
                d = self.driver.execute_script(open("scripts/second_products.js").read())
            return d
        except:
            return []

    def next_page(self):
        while True:
            try:
                if self.driver.execute_script('return document.querySelector("a.s-pagination-next")'):
                    counter = 0
                    while True:
                        try:
                            self.driver.execute_script('return document.querySelector("a.s-pagination-next").click()')
                            return True
                        except:
                            if counter == 50:
                                self.driver.refresh()
                                counter = 0
                            time.sleep(0.2)
                            counter += 1
                            pass
                return False
            except:
                pass


def scrape_product(url):
    driver = webdriver.Chrome(executable_path="a.exe")
    url = ast.literal_eval(url)
    if url["text"] == 'main menu':
        return True
    inst = StartScraping(driver, url["link"])
    inst.get_link()
    data = inst.get_products()
    if data:
        with open("product_links.txt", "a+") as myFile:
            for product_link in data:
                product_link["category"] = url["text"]
                myFile.write(f"{product_link}\n")
    while inst.next_page():
        time.sleep(1)
        data = inst.get_products()
        data_counter = 0
        while not data:
            if data_counter > 10:
                driver.refresh()
            data = inst.get_products()
            data_counter += 1
            time.sleep(0.3)

        while True:
            try:
                with open("product_links.txt", "a+") as myFile:
                    for product_link in data:
                        product_link["category"] = url["text"]
                        myFile.write(f"{product_link}\n")
                break
            except:
                time.sleep(0.1)
    driver.quit()


if __name__ == "__main__":
    threads = []
    with open("categories_links.txt", "r+") as cat:
        categories = cat.read().splitlines()
        while categories:
            selected_Category = categories[:3]
            for category in selected_Category:
                thread = threading.Thread(target=scrape_product, args=(category,))
                threads.append(thread)
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()
            threads = []
            categories = categories[3:]


