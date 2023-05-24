import pickle

initial_pickle = "D:\\Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\_pickles\\word_dutch.pkl"
unpickled_file = "D:\\Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\Output\\unpickled_dutch.py"

def unpickling_snake(dictionary, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("scraped_dutch = {\n")
        for key, value in dictionary.items():
            file.write(f"    '{key}': '{value}',\n")
        file.write("}")

with open(initial_pickle, 'rb') as file:
    scraped_dutch = pickle.load(file)

unpickling_snake(scraped_dutch, unpickled_file)
