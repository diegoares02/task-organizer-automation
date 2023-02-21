from selenium import webdriver
from selenium.webdriver.common.by import By


def test_eight_components():
    driver = webdriver.Chrome()

    driver.get("https://task-organizer-eee8c.firebaseapp.com")

    title = driver.title
    assert title == "React App"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.TAG_NAME, value="h1")
    assert text_box.text == "Task Organizer"

    driver.quit()