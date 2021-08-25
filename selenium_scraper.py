'''

Pure Selenium Webscraper.

'''


import random 
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver.exe") # Instance driver
driver.get('https://www.olx.com.co/portatiles-laptops_c1018') # Request
button = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')# click event to load information


# Interactions
for n in range(5):
    try:
        button.click()# Asyncrunous click
        sleep(random.uniform(5,10)) # Humanize behaviour
        button = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]') # Redefine new button instancen in DOM
    except:
        break

# After Interactions
products = driver.find_elements_by_xpath('//li[@class="EIR5N"]') #Return list
for product in products:    
    name =  product.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text
    price = product.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]').text
    location = product.find_element_by_xpath('.//span[@data-aut-id="item-location"]').text
    print(name, price, location)


driver.quit()