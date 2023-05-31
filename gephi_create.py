import csv
import pickle

def dictionary_to_CSV(original_file, nodes_target, edges_target):
    # Load data from pickle file
    with open(original_file, 'rb') as file:
        word_synonyms = pickle.load(file, encoding='latin1')

    # Create a set to store unique labels
    unique_labels = set()

    # Create nodes CSV file
    with open(nodes_target, 'w', newline='', encoding='utf-8', errors='ignore') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Id', 'Label'])
        for i, (word, targets) in enumerate(word_synonyms.items()):
            if targets is not None:
                # Lowercase the word and check if the lowercase label is unique
                lowercase_word = word.lower()
                if lowercase_word not in unique_labels:
                    writer.writerow([i, lowercase_word])
                    unique_labels.add(lowercase_word)

    # Create edges CSV file
    with open(edges_target, 'w', newline='', encoding='utf-8', errors='ignore') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Source', 'Target', 'Type'])
        for source, targets in word_synonyms.items():
            if targets is not None:
                source_index = list(unique_labels).index(source.lower())  # Get the index of the source word
                for target in targets:
                    lowercase_target = target.lower()
                    if lowercase_target in unique_labels:
                        target_index = list(unique_labels).index(lowercase_target)  # Get the index of the target word
                        writer.writerow([source_index, target_index, 'Directed'])

dictionary_to_CSV("Files/repickled_german.pkl", "german_nodes.csv", "german_edges.csv")
