import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
#import pandas as pd



email=['something@gia.com','blah@gia.com','ting@gia.com']
first_name_list=['abhishek','divyam','sumit','renu','lalit','nitish']
last_name_list=['sharma','gupta','malhotra','tiwari']
passport_detail_list=['hgfgwf768d9f','fbcdsjh76sf86','khhdsfd76sac','acds6csa8','caasc78acc','caacas6acac']
obtained_searchers=[]
expected_searcher=[319,23,260,45,79,34,262,201]
non_match = []

# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
driver=webdriver.Chrome()
driver.get("https://sg.via.com/")
# article_count=driver.find_element(By.CSS_SELECTOR,"#articlecount > a")
#
# print(article_count.text)
# article_count.click()
from_enter=driver.find_element(By.XPATH,"//*[@id='source']")
src_code=from_enter.send_keys("SIN")
from_enter.send_keys(Keys.ENTER)
first_option = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "ui-id-2")))
from_enter.send_keys(Keys.ARROW_DOWN)
# first_option = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".name")))
from_enter.send_keys(Keys.ENTER)

destination=driver.find_element(By.NAME,"destination")
dest_code=destination.send_keys("MNL")
destination.send_keys(Keys.ENTER)
second_option = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "ui-id-3")))
destination.send_keys(Keys.ARROW_DOWN)
destination.send_keys(Keys.ENTER)
# departure_date=driver.find_element(By.XPATH,"//*[@id='departure']").click()
# time.sleep(2)
departure_date_selection=WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="depart-cal"]/div[4]/div[2]/div[3]/div[5]'))).click()
search_button=driver.find_element(By.XPATH,"//*[@id='search-flight-btn']").click()

# time.sleep(30)
low_fare_container = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, "cheap_flight_container")))
tag_find=WebDriverWait(driver, 50).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,'.result')))
# tag_find=driver.find_elements(By.CSS_SELECTOR,".result")
time_list = [event.get_attribute("data-key") for event in tag_find]
print(time_list)
for x in time_list:
    start_index=(x.find("$"))+1
    print(start_index)
    last_index=x.find("_",x.find("_")+1)
    print(last_index)
    print(f"this is x:{x}")
    obatained_result=x[start_index:last_index]
    print(obatained_result)
    obtained_searchers.append(int(obatained_result))
obtained_unique_searchers=list(set(obtained_searchers))
print(obtained_unique_searchers)

def non_match_elements(list_a, list_b):
    non_match = []
    for i in list_a:
        if i not in list_b:
            non_match.append(i)
    return non_match
non_match = non_match_elements(expected_searcher,obtained_unique_searchers)
print("No match elements: ", non_match)
# print(obtained_searchers)
# csv_data={'EXPECTED_SEARCHER':{tuple(expected_searcher),'OBTAINED_SEARCHERS':tuple(obtained_searchers)
# df=pd.DataFrame(csv_data)
# df.style.set_caption(f"ROUTE{src_code}_{dest_code}")
# print(df)


# data_value=random.choice(time_list)
flight_code=input("Enter the flight Code")
flight="$"+f"{flight_code}"
print(flight)
res = [i for i in time_list if flight in i]
print(res)
data_value=random.choice(res)
print(data_value)

second_data_index=res.index(data_value)
orginal_data_index=time_list.index(data_value)
print(orginal_data_index)
data_index=orginal_data_index+3
print(data_value)
print(orginal_data_index)
print(data_index)


tag_find=driver.find_element(By.XPATH,f'//*[@id="searchResultContainer"]/div[4]/div/div[{data_index}]/div[1]/div[3]/button' ).click()

contact_info=driver.find_element(By.ID,"contactMobile")
number='8'
for i in range(9):
    number += random.choice('0123456789')

print(number)
contact_info.send_keys(number)

contact_email=driver.find_element(By.ID,"contactEmail")
contact_email.send_keys(random.choice(email))
proceed=driver.find_element(By.ID,"stp1Proceed")
proceed.click()

WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,'travCard')))


title=Select(driver.find_element(By.ID,"title-0"))
title_value=random.choice([x.text for x in title.options])
time.sleep(1)
title.select_by_value(title_value)

first_name=driver.find_element(By.ID,"fName-0")
first_name.send_keys(random.choice(first_name_list))

last_name=driver.find_element(By.ID,"lName-0")
last_name.send_keys(random.choice(last_name_list))

dob_day=Select(driver.find_element(By.ID,"dob-d-0"))
dob_day_value=random.choice([x.text for x in dob_day.options])
dob_day.select_by_value(dob_day_value)

dob_month=Select(driver.find_element(By.ID,"dob-m-0"))
dob_month_value=random.choice([x.text for x in dob_month.options])
print(dob_month_value)
dob_month.select_by_visible_text(dob_month_value)

dob_year=Select(driver.find_element(By.ID,"dob-y-0"))
list_year=[x.text for x in dob_year.options]
dob_list_year=list_year[7:]
dob_year_value=random.choice(dob_list_year)
dob_year.select_by_value(dob_year_value)

passport_detail=driver.find_element(By.ID,"num-0")
passport_detail.send_keys(random.choice(passport_detail_list))

doe_day=Select(driver.find_element(By.ID,"doe-d-0"))
doe_day_value=random.choice([x.text for x in doe_day.options])
doe_day.select_by_value(doe_day_value)

doe_month=Select(driver.find_element(By.ID,"doe-m-0"))
doe_month_value=random.choice([x.text for x in doe_month.options])
doe_month.select_by_visible_text(doe_month_value)

doe_year=Select(driver.find_element(By.ID,"doe-y-0"))
doe_list_year=[x.text for x in doe_year.options]
doe_year_value=random.choice(doe_list_year)
doe_year.select_by_value(doe_year_value)
time.sleep(2)
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="read_terms"]')))
element_to_click = driver.find_element(By.XPATH,'//*[@id="read_terms"]')
driver.execute_script("arguments[0].click();", element_to_click )

payment_page=driver.find_element(By.ID,"makePayCTA")
payment_page.click()




# titles=
# print(titles)


