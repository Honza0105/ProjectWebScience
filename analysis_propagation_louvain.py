import networkx as nx
import pickle
import time
import random

def label_propagation(graph, max_iterations=10):
    # Initialize labels
    labels = {node: graph.nodes[node].get('label', node) for node in graph.nodes}

    # Main label propagation loop
    for iteration in range(max_iterations):
        # Create a copy of the current labels
        old_labels = labels.copy()

        # Iterate over each node in the graph
        for node in graph.nodes:
            # Get the labels of neighboring nodes
            neighbor_labels = [old_labels[neighbor] for neighbor in graph.successors(node) if old_labels[neighbor] is not None]

            # If there are neighboring labels, update the current node's label
            if neighbor_labels:
                # Count the occurrences of each label
                label_counts = {label: neighbor_labels.count(label) for label in neighbor_labels}

                # Find the label with the maximum count
                max_count = max(label_counts.values())

                # Get all labels with the maximum count
                max_labels = [label for label, count in label_counts.items() if count == max_count]

                # If there is a tie, randomly choose one label
                selected_label = random.choice(max_labels)

                # Update the current node's label
                labels[node] = selected_label

        # Check for label convergence
        if labels == old_labels:
            break

        # Print the labels after each iteration
        print(f"Iteration {iteration+1}: Labels - {labels}")

    # Combine labels for nodes that have multiple labels
    combined_labels = {}
    for node in graph.nodes:
        if node != 'None':
            neighbor_labels = [labels[neighbor] for neighbor in graph.successors(node) if labels[neighbor] is not None]
            combined_labels[node] = '/'.join(set(neighbor_labels))

    # Return the final labels
    return combined_labels

# Load your graph from the pickled file
with open('Files/word_dutch.pkl', 'rb') as f:
    graph_dict = pickle.load(f)

# Create an empty NetworkX DiGraph
graph = nx.DiGraph()

# Iterate over the dictionary and add nodes and edges to the graph
for node, target_list in graph_dict.items():
    if target_list is not None:
        # Exclude nodes with None values
        if node != 'None' and len(target_list) > 2:
            graph.add_node(node, label=node)  # Assign label as the key itself
            for target in target_list:
                if target is not None:
                    # Create new node if it doesn't exist
                    if target not in graph.nodes:
                        graph.add_node(target, label=target)  # Assign label as the value
                    graph.add_edge(node, target)

# Start the stopwatch
start_time = time.time()

# Apply label propagation algorithm with a maximum of 10 iterations
final_labels = label_propagation(graph, max_iterations=10)

# Stop the stopwatch and calculate the elapsed time
elapsed_time = time.time() - start_time

# Print the final labels
print("Final Labels:", final_labels)

# Count the number of unique labels
unique_labels = len(set(final_labels.values()))

# Print the number of unique labels
print("Number of Unique Labels:", unique_labels)

# Print the elapsed time
print("Elapsed Time:", elapsed_time, "seconds")

print(graph)
