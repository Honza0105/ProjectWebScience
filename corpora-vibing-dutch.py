import csv
import re

initial_corpora = "D:\\Mano\\_Uni\\NL\\NL year 2\\4.5 project\\corpora\\nld_news_2022_1M\\nld_news_2022_1M-words.txt"
shortnened_corpora = "D:\\Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\Output\\output-nld_news_2022_1M-words.txt"

unique_words = set()
removed_words = set()

# Open the TSV and CSV files
with open(initial_corpora, "r", encoding="utf-8") as file_in, open(shortnened_corpora, "w", newline="", encoding="utf-8") as file_out:
    initial_corpora_reader = csv.reader(file_in, delimiter="\t")  # Create a TSV reader

    shortnened_corpora_writer = csv.writer(file_out)  # Create a CSV writer
    for row in initial_corpora_reader:
        if len(row) >= 3:
            word = row[1].lower()  # Convert the word to lowercase
            word = word.replace(".", "")
            word = word.replace("’", "")
            word = word.replace("”", "")
            word = word.replace("‘", "")
            word = word.replace(",", " ")
            word = word.replace("  ", " ")
            word = re.sub(r"\d", "", word)  # Remove numbers from the word
            if word in unique_words:
                removed_words.add(word)  # Add the lowercase word to the set of duplicate words
            else:
                unique_words.add(word)  # Add the lowercase word to the set of unique words
                shortnened_corpora_writer.writerow([word])  # Write the lowercase word to the CSV file
            
# Write the duplicate words to a separate file
removed_duplicates = "D:\\Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\Output\\removed_words-output-nld_news_2022_1M-words.txt"
with open(removed_duplicates, "w", encoding="utf-8") as file_duplicate:
    for word in removed_words:
        file_duplicate.write(word + "\n")
