import pickle
import time

import selenium
import stopwatch
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from stopwatch import Stopwatch
from webdriver_manager.chrome import ChromeDriverManager
from stopwatch import Stopwatch

def clean_up(text):
    if "Synonymgruppe" not in text:
        return None
    words_to_extract = ("Synonymgruppe", "ugs.", "ugs.,", "schweiz.", "ironisch",
                        "sarkastisch", "lat.", "österr","Abkürzung","fachspr.",
                        "[Hinweis: weitere Informationen erhalten Sie durch Ausklappen des Eintrages]",
                        "Linguistik/Sprache","Jargon","●","\n","'", "engl.", "veraltet", "Hauptform",
                        "geh.")
    for word in words_to_extract:
        text = text.replace(word, "")

    return text.split("·")


def clean_up(text, words_to_extract):
    if "Synonymgruppe" not in text:
        return None
    text = text.replace("●","·")
    text = text.replace("Synonymgruppe", "·")
    # words_to_extract = ("ugs.", "ugs.,", "schweiz.", "ironisch",
    #                     "sarkastisch", "lat.", "österr.","Abkürzung","fachspr.",
    #                     "[Hinweis: weitere Informationen erhalten Sie durch Ausklappen des Eintrages]",
    #                     "Linguistik/Sprache","Jargon","\n", "  ", "Verballhornung",",",
    #                     "Geschichte","Politik","Hauptform","Computer","Technik", "Scheinanglizismus",
    #                     "Markenname","scherzhaft","griechisch","werbesprachlich","Verballhornung","offiziell")
    ##add delete everything within brackets
    for word in words_to_extract:
        text = text.replace(word, "")
    Array = text.split("·")
    Array = [item.strip() for item in Array if item.strip()]  # Remove empty items
    return Array

def get_all_synonyms(word, driver):
    address = "https://www.dwds.de/wb/" + word
    # print(address)

    # print("Driver initialized")
    try:
        driver.get(address)
    except selenium.common.exceptions.WebDriverException:
        time.sleep(1)
        return get_all_synonyms(word,driver)
    # Set up Selenium driver

# "/html/body/main/div[1]/div/div[1]/div[2]/div/div[9]/div/div[1]/div/div[3]"
# "/html/body/main/div[1]/div/div[1]/div[2]/div/div[9]/div/div[2]/div/div[3]"
# "/html/body/main/div[1]/div/div[1]/div[2]/div/div[9]/div/div[2]/div/div[3]/a[1]"

    # Find the element using the XPath
    bad_elements_set = set()
    try:

        bad_elements = driver.find_elements(by.By.CLASS_NAME,"ot-diasystematik")
        for bad_element in bad_elements:
            bad_elements_set.add(bad_element.text)
        # print(bad_elements_set)
    except selenium.common.exceptions.NoSuchElementException:
        print("nothing removed")

    try:
        element = driver.find_element(by.By.XPATH, "/html/body/main/div[1]/div/div[1]/div[2]/div/div[9]/div")
    except selenium.common.exceptions.NoSuchElementException:
        return None
    # Get the content of the element
    content = element.text

    content = clean_up(content)

    # classes = element.get_attribute("class")
    # print(classes)
    content = clean_up(content,bad_elements_set)

    # Print the content
    # print(content)

    return content

def add_to_dictionary(word):
    dutch_dictionary[word]=get_all_synonyms(word,driver)

def do_the_thing(input_file, output_file):
    counter = 0
    with open(input_file, 'r') as file:
        for line in file:
            word = line.strip()
            add_to_dictionary(word)
            counter += 1
            # time.sleep(1)
            # print(counter)
            # print(word)
            if counter%10 == 0:
                print(counter)
            if counter%100 == 0:
                with open(output_file, 'wb') as file_out:
                    pickle.dump(dutch_dictionary, file_out)
                    print(counter)
                    print(stopwatch.duration)
            if counter%10000 == 0:
                break
        with open(output_file, 'wb') as file_out1:
            pickle.dump(dutch_dictionary, file_out1)

dutch_dictionary = {}
options = Options()
options.add_argument("--headless")  # Run Chrome in headless mode

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
stopwatch = Stopwatch(2)
# get_all_synonyms("Deutschland", driver)
# get_all_synonyms("Haus", driver)

# get_all_synonyms("Wort", driver)
# get_all_synonyms("Lied", driver)
do_the_thing('german_source.txt', 'word_german.pkl')
# with open('word_german.pkl', 'rb') as file:
#     my_dictionary = pickle.load(file)
# print(my_dictionary)
stopwatch.stop()
driver.quit()
print(stopwatch.duration)