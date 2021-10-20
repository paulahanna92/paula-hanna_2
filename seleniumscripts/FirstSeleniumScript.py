from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import xlrd

workbook = xlrd.open_workbook("C:\\Users\\Paula\\PycharmProjects\\pythonProject\\seleniumscripts\\Data.xls")
sheet = workbook.sheet_by_name("userCredentials")
rows = sheet.nrows
cols = sheet.ncols
for row in range(0, rows, 1):
  for col in range(0, cols-1, 1):
    username = sheet.cell_value(row, col)
    password = sheet.cell_value(row, col+1)
    s=Service("C:\\Users\\Paula\\PycharmProjects\\pythonProject\\chromedriver.exe")
    driver=webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get("http://www.facebook.com")
    usernamebox = driver.find_element(By.NAME, "email")
    passwordbox = driver.find_element(By.NAME, "pass")
    submit = driver.find_element(By.NAME, "login")
    usernamebox.send_keys(username)
    passwordbox.send_keys(password)
    submit.click()
    time.sleep(10)
workbook = xlrd.open_workbook("C:\\Users\\Paula\\PycharmProjects\\pythonProject\\seleniumscripts\\Data.xls")
sheet = workbook.sheet_by_name("registeration")
rows = sheet.nrows
for row in range(0, rows, 1):
  for col in range(0, cols-1, 1):
    firstname = sheet.cell_value(row, col)
    lastname = sheet.cell_value(row, col + 1)
    email = sheet.cell_value(row, col + 2)
    re_email = sheet.cell_value(row, col + 3)
    password = sheet.cell_value(row, col + 4)
    day_of_birth = sheet.cell_value(row, col + 5)
    month_of_birth = sheet.cell_value(row, col + 6)
    year_of_birth = sheet.cell_value(row, col + 7)
    gen = sheet.cell_value(row, col + 8)
    s=Service("C:\\Users\\Paula\\PycharmProjects\\pythonProject\\chromedriver.exe")
    driver=webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get("http://www.facebook.com")
    driver.find_element(By.XPATH, "//*[text()='Create New Account']").click()
    time.sleep(3)
    driver.find_element(By.NAME, "firstname").send_keys(firstname)
    driver.find_element(By.NAME, "lastname").send_keys(lastname)
    driver.find_element(By.NAME, "reg_email__").send_keys(email)
    driver.find_element(By.NAME, "reg_email_confirmation__").send_keys(re_email)
    driver.find_element(By.ID, "password_step_input").send_keys(password)
    birthday = Select(driver.find_element(By.NAME, "birthday_day"))
    birthday.select_by_visible_text(day_of_birth)
    birthmonth = Select(driver.find_element(By.NAME, "birthday_month"))
    birthmonth.select_by_visible_text(month_of_birth)
    birthyear = Select(driver.find_element(By.NAME, "birthday_year"))
    birthyear.select_by_visible_text(year_of_birth)
    if gen == "Male":
        driver.find_element(By.XPATH, "//label[text()='Male']").click()
    elif gen == "Female":
        driver.find_element(By.XPATH, "//label[text()='Female']").click()
    else:
        driver.find_element(By.XPATH, "//label[text()='Custom']").click()
        time.sleep(3)
        customgender = Select(driver.find_element(By.NAME, "preferred_pronoun"))
        if sheet.cell_value(row, col + 9) == "1":
          customgender.select_by_value("1")
        elif sheet.cell_value(row, col + 9) == "2":
          customgender.select_by_value("2")
        else:
          customgender.select_by_value("6")
    driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()
    time.sleep(10)
print("Done Testing!")



