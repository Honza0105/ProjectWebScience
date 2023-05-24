import csv

# Example dictionary with words and synonyms
word_synonyms = {
    'apple': ['fruit', 'pomaceous fruit'],
    'banana': ['fruit', 'yellow fruit'],
    'carrot': ['vegetable', 'orange vegetable']
}

# Create an array with unique words
word_array = list(set(word_synonyms.keys()).union(*word_synonyms.values()))

# Create nodes CSV file
with open('nodes.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Index', 'Word'])
    for i, word in enumerate(word_array):
        writer.writerow([i, word])

# Create edges CSV file
with open('edges.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Source', 'Target', 'Type'])
    for source, targets in word_synonyms.items():
        source_index = word_array.index(source)  # Get the index of the source word
        for target in targets:
            target_index = word_array.index(target)  # Get the index of the target word
            writer.writerow([source_index, target_index, 'Directed'])
