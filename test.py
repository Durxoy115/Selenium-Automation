from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service  # Corrected import
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
 
# Create a Chrome driver instance
options = Options()
options.add_argument("--start-maximized")
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)
 
 
# Visit the website
driver.get("http://13.58.91.85/#/login")
 
# Find the input element by XPath
wait = WebDriverWait(driver, 10)
input_element = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@name="userName"]')))
 
time.sleep(10)
# Perform actions on the input element
input_element.send_keys("admin@nq")  
time.sleep(10)
 
input_element1= wait.until(EC.visibility_of_element_located((By.NAME, "password")))
 
time.sleep(2)
 
# Perform actions on the input element
input_element1.send_keys("admin")  
time.sleep(2)

# Locate the login button using the provided XPath
login_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnLogin"]')))
time.sleep(2)
# Click the login button
login_button.click()
time.sleep(10)

#click an element
user_management = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[text()="User Management"]')))
user_management.click()
time.sleep(2)

# Wait for the element to be visible
user_element = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@title="User"]')))

# Click the element
user_element.click()

# Wait for the button to be clickable
add_new_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Add New")]')))

# Click the button
add_new_button.click()

# Use the correct tuple syntax for the locator
textbox_locator = (By.ID, 'phoneNo') 

# Wait for the text box to be visible
text_box1 = wait.until(EC.visibility_of_element_located(textbox_locator))

# Take input from the user
personal_id = input("Enter your Personal ID: ")

# Fill in the text box with user input
text_box1.send_keys(personal_id)

#  locator
input_name = (By.ID, 'fullName') 

# Wait for the input field to be visible
input_field = wait.until(EC.visibility_of_element_located(input_name))

# Take input from the user
user_input_name = input("Enter full name: ")

# Clear any existing text in the field
input_field.clear()  
# Fill in the input field with user input
input_field.send_keys(user_input_name)

#  locator
dropdown_locator = (By.NAME, 'departmentID') 

# Wait for the dropdown to be visible
dropdown = wait.until(EC.visibility_of_element_located(dropdown_locator))

# Create a Select object
select = Select(dropdown)

# Select the "QA" option by its visible text
select.select_by_visible_text('QA')

#  locator
desig_field_locator = (By.NAME, 'designation') 


# Wait for the input field to be visible
desig_field = wait.until(EC.visibility_of_element_located(desig_field_locator))

# Take input from the user
user_input_desig = input("Enter Designantion: ")

# Clear any existing text in the field
desig_field.clear()  
# Fill in the input field with user input
desig_field.send_keys(user_input_desig)

#  locator
country_locator = (By.NAME, 'country') 

# Wait for the dropdown to be visible
dropdown1 = wait.until(EC.visibility_of_element_located(country_locator))

# Create a Select object
select1 = Select(dropdown1)

# Select the "Bangladesh" option by its visible text
select1.select_by_visible_text('Bangladesh')

#  locator
phoneNumber_field_locator = (By.NAME, 'phoneNumber') 

# Wait for the dropdown to be visible
phoneNumber_field = wait.until(EC.visibility_of_element_located(phoneNumber_field_locator))

# Take input from the user
user_input_phoneNumber = input("Enter Phone Number: ")

# Clear any existing text in the field
phoneNumber_field.clear()  
# Fill in the input field with user input
phoneNumber_field.send_keys(user_input_phoneNumber)

# Wait for the checkbox to be clickable
checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='chkUser5']/input")))

#click
checkbox.click()

# Scroll down the page
driver.execute_script("window.scrollBy(0, 500);")
#locator on save button
save_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnSave"]')))
#click on Save Button
save_button.click()

#locator on 3dot
three_dot = wait.until( EC.visibility_of_element_located((By.XPATH, "(//button[@aria-label='Action menu'])[3]")))
       
#click on remove
three_dot.click()

#remove user
click_remove = wait.until( EC.visibility_of_element_located((By.XPATH, "//span[text()='Remove']")))

#click on remove
click_remove.click()

# Wait for the button to be clickable
yes_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Yes']")))

#click yes button to remove user

yes_button.click()

#find user icon locator
logout_field_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='fa ml-1 text-white cursor-pointer fa-chevron-down']")))

#click on icon
logout_field_locator.click()

#find logout button locator
logout_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Logout']")))

#click on Logout
login_button.click()
# Close the browser window
driver.quit()