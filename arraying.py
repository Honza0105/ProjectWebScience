import pickle

initial_pickle = "D:\\Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\_pickles\\word_dutch.pkl"
unpickled_nodes = "D:\\Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\Output\\unpickled_dutch_nodes.txt"
unpickled_edges = "D:\\Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\Output\\unpickled_dutch_edges.txt"

new_array = []

with open(initial_pickle, 'rb') as file:
    my_dictionary = pickle.load(file)

# Convert the dictionary to an array
for key, value in my_dictionary.items():
    if value is None:
        value = ""
    new_array.append({'key': key, 'value': value})

with open(unpickled_nodes, 'w', encoding='utf-8') as file:
# Save the dictionary as a human-readable file
    for entry in new_array:
        file.write(f"key: {entry['key']}\n")
        file.write(f"value: {entry['value']}\n")
        file.write('\n')
