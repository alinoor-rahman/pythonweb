import time
from selenium import webdriver
from selenium.webdriver.support.select import Select


# what to search
city_from = 'JSR'
city_to = 'CXB'
departure_date = '12-Dec-2018'

url = "https://secure.flynovoair.com/bookings/flight_selection.aspx"

driver = webdriver.Firefox()

driver.get(url)

# selct one wya from radio
driver.find_element_by_css_selector("input[type='radio'][value='OW']").click()


# select to from dropdown
select = Select(driver.find_element_by_name("DC"))
select.select_by_value(city_from)


# select destination from dropdown
select = Select(driver.find_element_by_name("AC"))
select.select_by_value(city_to)

input_departure_date = driver.find_element_by_id('AM1')
input_departure_date.clear()
input_departure_date.send_keys(departure_date)

driver.find_element_by_class_name("button").click()