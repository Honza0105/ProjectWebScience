import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from stopwatch import Stopwatch
from webdriver_manager.chrome import ChromeDriverManager
# Xpath1 = "/html/body/div/div[2]/div[1]/dl[1]"
Xpath2 = "/html/body/div/div[2]/div[1]/dl[2]"
# Xpath3 = "/html/body/div/div[2]/div[1]/dl[3]"

def clean_up(text, original_word):
    # if "Synonymgruppe" not in text:
    #     return None
    text = text.replace("\n",",")
    # text = text.replace("Synonymgruppe", "·")
    words_with_to_extract = (" (zn) :", " (bn) :"," (ww) :"," (vz) :")
    ##add delete everything within brackets
    for word in words_with_to_extract:
        text = text.replace(original_word+word, "")
    Array = text.split(",")
    Array = [item.strip() for item in Array if item.strip()]  # Remove empty items
    return Array


def get_all_synonyms(word, driver):
    address = "https://synoniemen.net/index.php?zoekterm=" + word
    # print(address)

    # print("Driver initialized")
    driver.get(address)
    # Set up Selenium driver

    # Find the element using the XPath
    try:
        element = driver.find_element(by.By.XPATH, "/html/body/div/div[2]/div[1]/dl[2]")
    except selenium.common.exceptions.NoSuchElementException:
        try:
            element = driver.find_element(by.By.XPATH,"/html/body/div/div[2]/div[1]/dl/dd")
        except selenium.common.exceptions.NoSuchElementException:
            return None
    # Get the content of the element
    content = element.text
    content = clean_up(content,word)
    # Print the content
    print(content)

    return content

options = Options()
options.add_argument("--headless")  # Run Chrome in headless mode

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
stopwatch = Stopwatch(2)
get_all_synonyms("fuck",driver)
print(stopwatch.duration)
get_all_synonyms("bij",driver)
print(stopwatch.duration)
get_all_synonyms("vertaling",driver)
print(stopwatch.duration)
get_all_synonyms("nederland",driver)
stopwatch.stop()
driver.quit()
print(stopwatch.duration)

