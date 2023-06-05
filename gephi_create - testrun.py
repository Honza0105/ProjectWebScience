import csv

def dictionary_to_CSV(word_synonyms, nodes_target, edges_target):
    # Create an array with unique words
    keys = word_synonyms.keys()
    value_sets = [set(v) for v in word_synonyms.values() if v is not None]
    union = set(keys).union(*value_sets)
    word_array = list(union)

    print(word_array)

    # Create nodes CSV file
    with open(nodes_target, 'w', newline='', encoding='utf-8', errors='ignore') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Id', 'Label'])
        for i, word in enumerate(word_array):
            writer.writerow([i, word.lower()])

    # Create edges CSV file
    with open(edges_target, 'w', newline='', encoding='utf-8', errors='ignore') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Source', 'Target', 'Type'])
        for source, targets in word_synonyms.items():
            source_index = word_array.index(source)  # Get the index of the source word
            if targets is not None:
                for target in targets:
                    target_index = word_array.index(target)  # Get the index of the target word
                    writer.writerow([source_index, target_index, 'Directed'])

unpickled_file = "D:\\Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\Output\\unpickled_german.py"

dictionary_to_CSV(unpickled_file, "german_nodes.csv", "german_edges.csv")
