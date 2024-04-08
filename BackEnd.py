import os

from dotenv import load_dotenv
from selenium import webdriver
import dotenv
from selenium.webdriver.common.by import By


def get_driver(headless=False):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless")
    return webdriver.Chrome(options=options)

def assignment_data(driver):
    assignment_classes = ["1069876"]
    content_classes = ["1069208", "1072688"]

    driver.get(f"https://mycourses.rit.edu/d2l/le/content/{content_classes[0]}/Home")
    driver.get(f"https://mycourses.rit.edu/d2l/lms/dropbox/user/folders_list.d2l?ou={assignment_classes[0]}&isprv=0")
    driver.get(f"https://mycourses.rit.edu/d2l/le/content/{content_classes[1]}/Home")

    for class_ID in content_classes:
        driver.get(f"https://mycourses.rit.edu/d2l/le/content/{class_ID}/Home")
        input()





def login(driver: webdriver):
    driver.get("https://mycourses.rit.edu/Shibboleth.sso/Login?entityID=https://shibboleth.main.ad.rit.edu/idp/shibboleth&target=https%3A%2F%2Fmycourses.rit.edu%2Fd2l%2FshibbolethSSO%2Flogin.d2l")
    driver.find_element(By.ID, "ritUsername").send_keys(os.getenv("USERNAME"))
    driver.find_element(By.ID, "ritPassword").send_keys(os.getenv("PASSWORD"))
    driver.find_element(By.NAME, "_eventId_proceed").click()
    input("press DUO")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver = get_driver()
    driver.get("Http://mycourses.rit.edu")
    load_dotenv()
    login(driver)
    assignment_data(driver)
    input("holdup")
