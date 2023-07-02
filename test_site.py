from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
# URL = 'https://...'
# LOGIN = 'test@test.ru'
# PASSWORD = 'passwrd'
#
#
# def get_driver():
#     chrome_options = Options()
#     chrome_options.add_argument("--window-size=1920,800")
#     chrome_options.add_argument("--headless")
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
#     driver.implicitly_wait(10)
#     return driver
#
#
# def open_page(driver, url):
#     driver.get(url)
#
#
# def get_element_by_id(driver, locator):
#     return driver.find_element(By.ID, locator)
#
#
# def element_click(driver, locator):
#     element = get_element_by_id(driver, locator)
#     element.click()
#
#
# def element_send_keys(driver, locator, text):
#     element = get_element_by_id(driver, locator)
#     element.send_keys(text)
#
#
# def open_login_page(driver):
#     element_click(driver, 'login-link')
#
#
# def login(driver, name, password):
#     element_send_keys(driver, 'name', name)
#     element_send_keys(driver, 'password', password)
#     element_click(driver, 'register')
#
#
# driver = get_driver()
# open_page(driver, URL)
# open_login_page()
# login(driver, name=LOGIN, password=PASSWORD)
#
# driver.quit()
