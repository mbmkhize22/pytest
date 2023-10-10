from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
# driver = webdriver.Chrome(executable_path="/path/to/chromedriver")
driver = webdriver.Chrome(executable_path="C:\ProgramData\chocolatey\lib\chromedriver\tools")

# Open the provided URL
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Radio Buttons
radio_button_3 = driver.find_element(By.XPATH, "//input[@value='radio3']")
radio_button_2 = driver.find_element(By.XPATH, "//input[@value='radio2']")

# Click on radio button 3 and validate
radio_button_3.click()
assert radio_button_3.is_selected()
assert not radio_button_2.is_selected()

# Click on radio button 2 and validate
radio_button_2.click()
assert radio_button_2.is_selected()
assert not radio_button_3.is_selected()

# Suggestion Field
suggestion_field = driver.find_element(By.ID, "autocomplete")
suggestion_field.send_keys("South")
time.sleep(1)  # Give time for suggestions to appear
suggestion_option = driver.find_element(By.CSS_SELECTOR, ".ui-menu-item div")
suggestion_option.click()
assert suggestion_field.get_attribute("value") == "South Africa"

suggestion_field.clear()
suggestion_field.send_keys("Republic")
time.sleep(1)
suggestion_option = driver.find_element(By.CSS_SELECTOR, ".ui-menu-item div")
suggestion_option.click()
assert suggestion_field.get_attribute("value") == "Republic of the Congo"

# Checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.click()
    assert checkbox.is_selected()

checkboxes[0].click()
for checkbox in checkboxes[1:]:
    assert checkbox.is_selected()

# Show/Hide Elements
hide_button = driver.find_element(By.ID, "hide-textbox")
show_button = driver.find_element(By.ID, "show-textbox")
hidden_element = driver.find_element(By.ID, "displayed-text")

hide_button.click()
assert not hidden_element.is_displayed()

show_button.click()
assert hidden_element.is_displayed()

# Web Table
table = driver.find_element(By.ID, "product")
rows = table.find_elements(By.TAG_NAME, "tr")

# Validate Amount for 'Joe Postman' from 'Chennai'
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    if len(cells) > 1 and cells[0].text == "Joe Postman" and cells[1].text == "Chennai":
        assert cells[2].text == "46"
        break

# Validate Total Amount Collected
total_amount = 0
for row in rows[1:]:  # Exclude the header row
    cells = row.find_elements(By.TAG_NAME, "td")
    total_amount += int(cells[2].text)

assert total_amount == 296

# iFrame
iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

# Interact with an element within the iframe (example: clicking a button)
iframe_button = driver.find_element(By.XPATH, "//button[contains(text(), 'I am inside an iframe')]")
iframe_button.click()

# Switch back to the default content
driver.switch_to.default_content()

# Close the browser
driver.quit()