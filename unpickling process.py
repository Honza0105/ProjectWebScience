import pickle

initial_pickle = "D:\\Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\_pickles\\word_german.pkl"
unpickled_file = "D:\\Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\Output\\unpickled_german.py"

def unpickling_the_snake(dictionary, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("scraped_german = {\n")
        for key in sorted(dictionary):
            value = dictionary[key]
            if value is not None:
                file.write(f"    {repr(key.lower())}: {repr(value.lower())},\n")
        file.write("}")

with open(initial_pickle, 'rb') as file:
    scraped_german = pickle.load(file)

unpickling_the_snake(scraped_german, unpickled_file)
