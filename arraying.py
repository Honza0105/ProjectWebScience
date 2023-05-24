import pickle

initial_pickle = "D:\\Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\_pickles\\word_dutch.pkl"
unpickled_file = "D:\\Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\Output\\unpickled_dutch.py"


def unpickling_snake(dictionary, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("scraped_dutch = {\n")
        for key, value in dictionary.items():
            file.write(f"    '{key}': {value},\n")
        file.write("}")

# Load the dictionary from the .pkl file
with open(initial_pickle, 'rb') as file:
    scraped_dutch = pickle.load(file)

# Save the dictionary as a .py file
unpickling_snake(scraped_dutch, unpickled_file)


new_array = []

with open(initial_pickle, 'rb') as file:
    scraped_dutch = pickle.load(file)

for key, value in scraped_dutch.items():
    if value is None:
        value = ""
    new_array.append({'key': key, 'value': value})

with open(unpickled_file, 'w', encoding='utf-8') as file:
    for entry in new_array:
        file.write(f"key: {entry['key']}\n")
        file.write(f"value: {entry['value']}\n")
        file.write('\n')
