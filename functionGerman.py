import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def getAllSynonyms(word):
    address = "https://www.dwds.de/wb/" + word
    print(address)
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(address)
    # Set up Selenium driver

    # Find the element using the XPath
    try:
        element = driver.find_element(by.By.XPATH,"/html/body/main/div[1]/div/div[1]/div[2]/div/div[9]/div")
    except selenium.common.exceptions.NoSuchElementException:
        return None
    # Get the content of the element
    content = element.text

    # Print the content
    # print(content)

    return content

    # Close the Selenium driver
    driver.quit()

print(getAllSynonyms("Servus"))
