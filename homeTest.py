import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import FirefoxOptions

@pytest.fixture(scope="class")
def setup(request):
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    driver = webdriver.Firefox(options=opts)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
@pytest.mark.usefixtures("setup")
class TestBase:
    pass
class TestTaskOrganizer(TestBase):
    def test_home(self):

        self.driver.get("https://task-organizer-eee8c.firebaseapp.com")

        title = self.driver.title
        assert title == "React App"
    
    def test_home_main_title(self):

        self.driver.get("https://task-organizer-eee8c.firebaseapp.com")

        self.driver.implicitly_wait(0.5)

        text_box = self.driver.find_element(by=By.TAG_NAME, value="h1")
        assert text_box.text == "Task Organizer"

    def test_open_modal(self):
        self.driver.get("https://task-organizer-eee8c.firebaseapp.com")

        self.driver.implicitly_wait(0.5)

        add_button = self.driver.find_element(by=By.XPATH, value="/html/body/div/div/button/i")
        add_button.click()
        modal_title = self.driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div/div[1]/div")

        assert modal_title.text == "Add new task"

    def test_add_task_error(self):
        self.driver.get("https://task-organizer-eee8c.firebaseapp.com")

        self.driver.implicitly_wait(0.5)

        add_button = self.driver.find_element(by=By.XPATH, value="/html/body/div/div/button/i")
        add_button.click()
        
        save_button = self.driver.find_element(by=By.XPATH,value="/html/body/div[3]/div/div/div[3]/button")
        save_button.click()

        modal_title = self.driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div/div[1]/div")

        assert modal_title.text == "Add new task"

    def test_add_task_successfully(self):
        self.driver.get("https://task-organizer-eee8c.firebaseapp.com")

        self.driver.implicitly_wait(0.5)

        add_button = self.driver.find_element(by=By.XPATH, value="/html/body/div/div/button/i")
        add_button.click()

        title_input = self.driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div/div[2]/form/div[1]/input")
        title_input.send_keys("Automated Test")
        
        save_button = self.driver.find_element(by=By.XPATH,value="/html/body/div[3]/div/div/div[3]/button")
        save_button.click()

        self.driver.implicitly_wait(2)

        assert "Automated Test" in self.driver.page_source

    def test_delete_task_card(self):
        self.driver.get("https://task-organizer-eee8c.firebaseapp.com")

        self.driver.implicitly_wait(0.5)        

        delete_button = self.driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[6]/div/div/div/button")
        delete_button.click()

        assert "Test 6" not in self.driver.page_source