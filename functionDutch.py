import selenium
import pickle
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from stopwatch import Stopwatch
from webdriver_manager.chrome import ChromeDriverManager
# Xpath1 = "/html/body/div/div[2]/div[1]/dl[1]"
Xpath2 = "/html/body/div/div[2]/div[1]/dl[2]"
# Xpath3 = "/html/body/div/div[2]/div[1]/dl[3]"

my_dictionary = {}

def clean_up(text, original_word):
    # if "Synonymgruppe" not in text:
    #     return None
    text = text.replace("\n",",")
    # text = text.replace("Synonymgruppe", "·")
    words_with_to_extract = (" (zn) :", " (bn) :"," (ww) :"," (vz) :"," (tw) :","(bw)"," (vnw) :","(vnw)","(vw)","(ww)","(bw)")
    ##add delete everything within brackets
    for word in words_with_to_extract:
        text = text.replace(original_word+word, "")
        text = text.replace(word, "")
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

        element = driver.find_element(by.By.XPATH, "/html/body/div/div[2]/div[1]/p[1]")

        if element.text == "als trefwoord met bijbehorende synoniemen:":
            element = driver.find_element(by.By.XPATH, "/html/body/div/div[2]/div[1]/dl[1]")
        else:
            element = driver.find_element(by.By.XPATH, "/html/body/div/div[2]/div[1]/p[2]")
            if element.text == "als trefwoord met bijbehorende synoniemen:":
                element = driver.find_element(by.By.XPATH, "/html/body/div/div[2]/div[1]/dl[2]")
            else:
                return None

    except selenium.common.exceptions.NoSuchElementException as op:
        print(op)
        print(word)
        time.sleep(6)
        return get_all_synonyms(word,driver)
    # Get the content of the element
    content = element.text
    content = clean_up(content,word)
    # Print the content
    # print(content)

    return content


def add_to_dictionary(word):
    my_dictionary[word]=get_all_synonyms(word,driver)

def do_the_thing(input_file, output_file):
    counter = 0
    with open(input_file, 'r') as file:
        for line in file:
            word = line.strip()
            add_to_dictionary(word)
            counter += 1
            time.sleep(1)
            print(counter)
            print(word)
            if counter%10 == 0:
                with open(output_file, 'wb') as file_out:
                    pickle.dump(my_dictionary, file_out)
                    print(counter)
            if counter%35 == 0:
                break
        with open(output_file, 'wb') as file_out1:
            pickle.dump(my_dictionary, file_out1)

            # Perform additional operations with the word as needed


options = Options()
options.add_argument("--headless")  # Run Chrome in headless mode

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
stopwatch = Stopwatch(2)

# get_all_synonyms("fuck",driver)
# print(stopwatch.duration)
# get_all_synonyms("met",driver)
# print(stopwatch.duration)
# get_all_synonyms("vertaling",driver)
# print(stopwatch.duration)
# get_all_synonyms("erik",driver)
# add_to_dictionary("fuck")
# add_to_dictionary("met")
# add_to_dictionary("vertaling")
# add_to_dictionary("erik")
# add_to_dictionary("bij")

# print(stopwatch.duration)
# print(my_dictionary)
# with open('dictionary.pkl', 'wb') as file:
#     pickle.dump(my_dictionary, file)
#Example: Printing all key-value pairs
# for key, value in my_dictionary.items():
#     print(key, value)
# add_to_dictionary("bij")
# print(my_dictionary)
do_the_thing('dutch_word.txt', 'word_dutch.pkl')
with open('word_dutch.pkl', 'rb') as file:
    my_dictionary = pickle.load(file)
# print(len(my_dictionary))
print(my_dictionary)
stopwatch.stop()
print(stopwatch)
driver.quit()
