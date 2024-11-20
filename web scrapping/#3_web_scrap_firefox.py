from selenium import webdriver 


from selenium.webdriver.firefox.service import Service 


path=r'C:\Desktop\DATA-SCIENCE-AND-MACHINE-LEARNING\DATA-SCIENCE\web scrapping\geckodriver.exe'
website='https://www.linkedin.com/feed/'



driver=webdriver.Firefox(service=Service(path))

