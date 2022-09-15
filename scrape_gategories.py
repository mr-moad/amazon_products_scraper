from selenium import webdriver
import time


def get_categories():
    driver = webdriver.Chrome(executable_path="a.exe")
    driver.get("https://amazon.com")
    time.sleep(1)
    driver.execute_script('return document.getElementById("nav-hamburger-menu")').click()
    time.sleep(0.3)
    links = driver.execute_script(open("scripts/grab_links.js").read())
    with open("categories_links.txt", "a+") as cat:
        for link in links:
            if link["link"] != "https://www.amazon.com/":
                cat.writelines(f"{link}\n")
    driver.quit()


if __name__ == "__main__":
    get_categories()