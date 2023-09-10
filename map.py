import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import openpyxl

service = Service(
    r"C:\Users\koush\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

file_path = r"C:\Users\koush\Downloads\AesCliMal.xlsx"
workbook = openpyxl.load_workbook(file_path)
worksheet = workbook.active


def lol(x, y):
    driver.get(
        f"https://www.google.com/maps/search/Aesthetic+Clinic+in+kuala+lumpur/@{x},{y},14z/data=!4m4!2m3!5m1!4e9!6e1?entry=ttu"
    )
    print(driver.current_url)
    driver.implicitly_wait(10)
    divx = driver.find_element(
        "xpath", "//div[@aria-label='Results for Aesthetic Clinic in kuala lumpur']"
    )
    w = 150
    while w:
        driver.execute_script("arguments[0].scrollBy(0, 1000000);", divx)
        w -= 1
        time.sleep(0.1)
    links = driver.find_elements("xpath", "//a[@href]")
    for link in links:
        href = link.get_attribute("href")
        worksheet.append([href])
        print(href)


x = 3.056058
while x < 3.218067:
    y = 101.647851
    while y < 101.748686:
        y += 0.1
        lol(x, y)
    x += 0.1

workbook.save(file_path)
workbook.close()
driver.quit()
