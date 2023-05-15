from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up Selenium driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.dwds.de/wb/Auto")

# Find the element using the XPath
element = driver.find_element_by_xpath("/html/body/main/div[1]/div/div[1]/div[2]/div/div[9]/div")

# Get the content of the element
content = element.text

# Print the content
print(content)

# Close the Selenium driver
driver.quit()
