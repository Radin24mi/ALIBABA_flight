from logging import exception

from selenium.webdriver.common.by import By
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlalchemy
import pyodbc
import pymysql
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


#خوندن سایت
driver = webdriver.Chrome()
driver.get("https://www.alibaba.ir/flights/THR-SYZ?adult=1&child=0&infant=0&departing=1404-06-21&returning=1404-06-28")

#خوندن صفحه پرواز اول
flights = driver.find_elements(By.CSS_SELECTOR, ".available-card")



fly_list = []
#پیدا کردن داده های پرواز اول
for flight in flights:
    try:
        spans = flight.find_elements(By.TAG_NAME, "span")
        data = {}

        for s in spans:
         print(s.text)

        data["full_text"] = flight.text
        fly_list.append(data)

        # class, plain code, origin, dest, price, fly number , seat left
        flight1 = "flight1",flight.find_element(By.CSS_SELECTOR, ".gap-2").text
        print(flight1)

        class_span = flight.find_element(
            By.XPATH, "//span[@class='text-headline-sm text-grays-600' and text = 'اکونومی']/following-sibling::span"
        )
        print("کلاس پروازی:", class_span.text)


        plain_code = flight.find_element(
            By.XPATH, "//span[@class='text-headline-sm text-grays-600' and text = 'A319']/following-sibling::span"
        )
        print("مدل هواپیما:", plain_code.text)


        origin = flight.find_element(
            By.XPATH, "//span[@class='flex gap-2 items-center' and text = 'تهران']/following-sibling::span"
        )
        print("مبدا:", origin.text)

        dest = flight.find_element(
            By.XPATH, "//span[@class='flex flex-1 gap-2 items-center' and text = 'شیراز']/following-sibling::span"
        )
        print("مقصد:", dest.text)

        price = flight.find_element(By.CSS_SELECTOR, ".block strong").text
        print(price)

        fly_number = flight.find_element(
            By.XPATH, "//span[@class='text-headline-sm text-grays-600' and text = '232']/following-sibling::span"
        )
        print("شماره پرواز::", fly_number.text)

        seat_left = flight.find_element(
            By.XPATH, "//span[@class='ml-1' and text = '232']/following-sibling::span"
        )
        print("شماره پرواز::", seat_left.text)


        print("مقصد:", origin.text)




        system, plain_code, origin, dest, price, fly_number , seat_left = flight.find_elements(By.CSS_SELECTOR, "gap-2").text.split("\n")
        data["system"] = system
        data["plain_code"] = plain_code
        data["origin"] = origin
        data["dest"] =dest
        data["price"] = price
        data["fly_number"] = fly_number
        data["seat left"] = seat_left
        fly_list.append(data)

    except Exception as e:
        print("Error:", e)
        continue



time.sleep(5)

driver.close()

#وارد کردن اطلاعات به اکسل (ناموفق)


df = pd.DataFrame(fly_list)

df.to_csv("flight3.csv", index = False , encoding = "utf-8-sig")
