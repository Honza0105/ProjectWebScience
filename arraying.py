import pickle

initial_pickle = "D:\\Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\_pickles\\word_dutch.pkl"
unpickled_nodes = "D:\\Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\Output\\unpickled_dutch_nodes.txt"
unpickled_edges = "D:\\Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\Output\\unpickled_dutch_edges.txt"

new_array = []

with open(initial_pickle, 'rb') as file:
    my_dictionary = pickle.load(file)

# Convert the dictionary to an array
for key, value in my_dictionary.items():
    new_array.append({'key': key, 'value': value})

# Print the new array
for item in new_array:
    print(item)
