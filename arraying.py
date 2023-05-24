import csv
import re
import pickle

initial_pickle = "D:\\Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\_pickles\\word_dutch.pkl"
unpickled_nodes = "D:\\Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\Output\\unpickled_dutch_nodes.txt"
unpickled_edges = "D:\\Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\Output\\unpickled_dutch_edges.txt"

new_array = []

with open(initial_pickle, 'rb') as file:
    my_dictionary = pickle.load(file)

new_array.append(my_dictionary)

with open(unpickled_nodes, "w", encoding="utf-8") as file_duplicate:
    for word in new_array:
        unpickled_edges.write(word + "\n")

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

my_array = [{'key': key, 'value': value} for key, value in my_dict.items()]

print(my_array)


# print(new_array)

# if thing is not None:
#     print()