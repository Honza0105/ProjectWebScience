import csv
import pickle

def dictionary_to_CSV(original_file, nodes_target, edges_target):
    # Load data from pickle file
    with open(original_file, 'rb') as file:

    # for key in word_synonyms.keys():
    #     print(key)



        word_synonyms = pickle.load(file, encoding='unicode_escape')

    # Create an array with unique words
    # word_array = list(set(word_synonyms.keys()).union(*word_synonyms.values()))
    keys = word_synonyms.keys()
    value_sets = [set(v) for v in word_synonyms.values() if v is not None]
    union = set(keys).union(*value_sets)
    word_array = list(union)

    print(word_array)



    # Create nodes CSV file
    with open(nodes_target, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Id', 'Label'])
        for i, word in enumerate(word_array):
            writer.writerow([i, word])

    # Create edges CSV file
    with open(edges_target, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Source', 'Target', 'Type'])
        for source, targets in word_synonyms.items():
            source_index = word_array.index(source)  # Get the index of the source word
            if targets is not None:
                for target in targets:
                    target_index = word_array.index(target)  # Get the index of the target word
                    writer.writerow([source_index, target_index, 'Directed'])

dictionary_to_CSV("Files/repickled_german.pkl", "german_nodes.csv", "german_edges.csv")
