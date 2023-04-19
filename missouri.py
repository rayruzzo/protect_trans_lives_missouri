
# Import the necessary libraries
import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

##################################################
# Create a fake Missouri Citizen
fake_person = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()))
fake_person.get('https://www.fakenamegenerator.com/gen-random-us-us.php')

# Use XPATH to get their name
fake_name = fake_person.find_element(
    By.XPATH, "//div[@class='address']/h3").text
first_name = fake_name.split()[0]
last_name = fake_name.split()[-1]

# Iterate through the information to get their email
email_string = "Email Address"
information = fake_person.find_elements(
    By.XPATH, "//dl[@class='dl-horizontal']")
for info in information:
    if email_string in info.find_element(By.TAG_NAME, "dt").text:
        fake_email = info.find_element(By.TAG_NAME, "dd").text.split()[0]

# Exit the fake person
fake_person.quit()

# Create fake address for the fake person
fake_location = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()))
fake_location.get(
    'https://www.fakeaddresscopy.com/usa/USA_city/Missouri/')

# Use XPATH to get the address
fake_address = fake_location.find_element(By.XPATH, "//input[@id='copyInput5']").get_attribute("value")
fake_location.quit()


street = fake_address.split(",")[0]
city = fake_address.split(",")[1]
state = "MO"
zip_code = fake_address.split(",")[-1][0:6]

fake_location.quit()

##################################################

# Select a random senator to report
reporting_republican = random.choice(['Dan W. Brown', 'Eric Burlison', 'Mike Cierpiot', 'Bill Eigel', 'Denny Hoskins', 'Lincoln Hough', 'Andrew Koenig', 'Bob Onder', 'Mike Moon', 'Caleb Rowden', 'David Sater', 'E. Eric Burlison', 'Holly Rehder', 'Tony Luetkemeyer', 'Rick Brattin', 'Sandy Crawford', 'Justin Brown', 'Kathryn Swan', 'Michael Davis', 'Cindy OLaughlin', 'Hannah Kelly', 'Caleb Rowden', 'Don Mayhew', 'Bill Kidd', 'Adam Schnelting', 'Mike Haffner', 'Doug Richey', 'Cheri Toalson Reisch', 'Travis Fitzwater', 'Mike Stephens', 'John Wiemann',]
                                      )
message = f"I am suspicious that {reporting_republican} is transgender and has sought transgender surgery. You need to investigate this immediately."

##################################################

# Get the page for the bullshit trans complaint form
browser = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()))
browser.get('https://ago.mo.gov/file-a-complaint/transgender-center-concerns')

# Fill out the form
browser.find_element(By.ID, "Textbox-1").send_keys(first_name)
browser.find_element(By.ID, "Textbox-2").send_keys(last_name)
browser.find_element(By.ID, "Textbox-6").send_keys(fake_email)
browser.find_element(By.ID, "Textbox-3").send_keys(street)
browser.find_element(By.ID, "Textbox-4").send_keys(city)
browser.find_element(By.ID, "Dropdown-1").send_keys(state)
browser.find_element(By.ID, "Textbox-5").send_keys(zip_code)
browser.find_element(By.ID, "Textarea-1").send_keys(message)
time.sleep(5)


continue_button = browser.find_element(By.XPATH, value="//button[@type='submit']")
continue_button.click()

time.sleep(5)
browser.quit()
