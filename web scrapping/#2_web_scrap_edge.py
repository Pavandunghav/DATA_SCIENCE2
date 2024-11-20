# from selenium import webdriver 
# from selenium.webdriver.edge.service import Service 

# path=r'C:\Desktop\DATA-SCIENCE-AND-MACHINE-LEARNING\DATA-SCIENCE\web scrapping\msedgedriver.exe'
# website="https://www.linkedin.com/feed/"



# driver=webdriver.Edge(service=Service(path))
# driver.get(website)



from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

# Path to the Edge WebDriver
path = r'C:\Desktop\DATA-SCIENCE-AND-MACHINE-LEARNING\DATA-SCIENCE\web scrapping\msedgedriver.exe'

# URL to visit
website = "https://www.linkedin.com/login"

# Initialize Edge options
options = Options()
# Add any specific options if needed
# options.add_argument("--headless")  # Uncomment to run in headless mode if necessary

# Set up the Edge WebDriver service
service = Service(executable_path=path)

# Initialize the WebDriver with the service
driver = webdriver.Edge(service=service, options=options)

# Open the website
driver.get(website)

# Perform any additional actions if necessary
# For example, login to LinkedIn or interact with the page elements
# Example (pseudo-code for login):
# username_field = driver.find_element(By.ID, "username")
# password_field = driver.find_element(By.ID, "password")
# login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
# username_field.send_keys("your_username")
# password_field.send_keys("your_password")
# login_button.click()

# Close the browser after operations
# driver.quit()

