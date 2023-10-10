import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service



service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
#driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

driver.get('http://www.google.com/')

time.sleep(5000) # Let the user actually see something!

search_box = driver.find_element_by_name('q')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5000) # Let the user actually see something!

driver.quit()