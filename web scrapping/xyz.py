from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
from selenium.webdriver.edge.service import Service


# def login(driver, username, password):
#     driver.get("https://www.linkedin.com/login")

#     try:
#         username_input = driver.find_element(By.ID, "username")
#         password_input = driver.find_element(By.ID, "password")
#         login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

#         username_input.send_keys(username)
#         password_input.send_keys(password)
#         login_button.click()

#         # Wait for login to complete, assuming a profile link appears upon successful login
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.ID, "profile-nav-item"))
#         )
#         print("Login successful")
#     except Exception as e:
#         print(f"Login failed: {e}")
#         driver.quit()

def scrape_data(driver):
    # Navigate to the data page
    driver.get("https://www.linkedin.com/feed")

    # Wait for the data to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "feed-shared-update-v2"))
    )

    # Extract data
    data_elements = driver.find_elements(By.CLASS_NAME, "feed-shared-update-v2")
    data = [element.text for element in data_elements]

    # Save data to CSV
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Data"])
        for item in data:
            writer.writerow([item])

    print("Data scraped and saved to data.csv")

def main():
    username = "pavan.dunghav03@gmail.com"
    password = "#Pav@n20-06"
    
    
    
    

    options = webdriver.EdgeOptions()
    options.add_argument("--headless")  # Run in headless mode
    driver_path = r'C:\Desktop\DATA-SCIENCE-AND-MACHINE-LEARNING\DATA-SCIENCE\web scrapping\msedgedriver.exe'  # Specify the path to msedgedriver
    driver = webdriver.Edge(service=Service(driver_path), options=options)

    try:
        #login(driver, username, password)
        scrape_data(driver)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
