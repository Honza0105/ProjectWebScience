import selenium
import stopwatch
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from stopwatch import Stopwatch

def clean_up(text):
    if "Synonymgruppe" not in text:
        return None
    words_to_extract = ("Synonymgruppe", "ugs.", "·", "ugs.,", "schweiz.", "ironisch",
                        "sarkastisch", "lat.", "österr","Abkürzung","fachspr.",
                        "[Hinweis: weitere Informationen erhalten Sie durch Ausklappen des Eintrages]",
                        "Linguistik/Sprache","Jargon")
    for word in words_to_extract:
        text = text.replace(word, "")

    return text.split(".")



def get_all_synonyms(word, driver):
    address = "https://www.dwds.de/wb/" + word
    # print(address)

    # print("Driver initialized")
    driver.get(address)
    # Set up Selenium driver

    # Find the element using the XPath
    try:
        element = driver.find_element(by.By.XPATH, "/html/body/main/div[1]/div/div[1]/div[2]/div/div[9]/div")
    except selenium.common.exceptions.NoSuchElementException:
        return None
    # Get the content of the element
    content = element.text
    content = clean_up(content)
    # Print the content
    print(content)

    return content


options = Options()
options.add_argument("--headless")  # Run Chrome in headless mode

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

get_all_synonyms("Deutschland", driver)
get_all_synonyms("Handy", driver)
get_all_synonyms("Wort", driver)
get_all_synonyms("Lied", driver)

driver.quit()
