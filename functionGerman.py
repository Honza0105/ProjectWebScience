from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from webdriver_manager.chrome import ChromeDriverManager


def getAllSynonyms(word):
    address = "https://www.dwds.de/wb/" + word
    print(address)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(address)
    # Set up Selenium driver

    # Find the element using the XPath
    element = driver.find_element(by.By.XPATH,"/html/body/main/div[1]/div/div[1]/div[2]/div/div[9]/div")

    # Get the content of the element
    content = element.text

    # Print the content
    print(content)

    # Close the Selenium driver
    driver.quit()

getAllSynonyms("Auto")
