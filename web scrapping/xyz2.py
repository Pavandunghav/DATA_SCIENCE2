from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd

from selenium.webdriver.edge.service import Service 
# Replace these with your LinkedIn credentials
linkedin_username = 'pavan.dunghav03@gmail.com'
linkedin_password = '#Pav@n20-06'


path=r"C:\Desktop\DATA-SCIENCE-AND-MACHINE-LEARNING\DATA-SCIENCE\web scrapping\msedgedriver.exe"
# Initialize the Chrome driver
driver = webdriver.Edge(service=Service(path))

# Open LinkedIn login page
driver.get('https://www.linkedin.com/login')

# Log in to LinkedIn
username_field = driver.find_element(By.ID, 'username')
username_field.send_keys(linkedin_username)

password_field = driver.find_element(By.ID, 'password')
password_field.send_keys(linkedin_password)
password_field.send_keys(Keys.RETURN)

# Wait for login to complete
time.sleep(30)

# Navigate to the LinkedIn feed
driver.get('https://www.linkedin.com/jobs/')

# Wait for the feed to load
time.sleep(10)

# Get the page source and parse it with BeautifulSoup
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# Extract the posts
posts = soup.find_all('div', {'class': 'occludable-update'})

# Prepare a list to store the extracted data
data = []

for post in posts:
    try:
        author = post.find('span', {'class': 'feed-shared-actor__name'}).get_text(strip=True)
        content = post.find('span', {'class': 'feed-shared-text__text-view'}).get_text(strip=True)
        timestamp = post.find('span', {'class': 'feed-shared-actor__sub-description'}).get_text(strip=True)
        data.append({'Author': author, 'Content': content, 'Timestamp': timestamp})
    except AttributeError:
        continue

# Convert the list to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('linkedin_feed.csv', index=False)

# Close the browser
driver.quit()
