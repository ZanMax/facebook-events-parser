from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import wait_until_page_load
from bs4 import BeautifulSoup

LOGIN_URL = 'https://m.facebook.com/login.php'
LOGIN_EMAIL = ''
LOGIN_PASSWORD = ''
DEBUG = True

if DEBUG:
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
else:
    driver = webdriver.Chrome()

driver.get(LOGIN_URL)
driver.find_element(By.ID, 'm_login_email').send_keys(LOGIN_EMAIL)
driver.find_element(By.ID, 'm_login_password').send_keys(LOGIN_PASSWORD)
driver.find_element(By.NAME, 'login').click()

wait_until_page_load(driver)

driver.get("https://m.facebook.com/groups/<group_id>/?view=events")
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
# result = soup.find('article', class_=['2ycp', '_5xhk'])
article = soup.find('article')
divs = article.findAll('div')
for div in divs:
    name = div.find('h4')
    if name:
        print(name.text)
        print('------------------')
    link = div.find('a')
    if link:
        print(link['href'])
        print('------------------')
driver.close()
