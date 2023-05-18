import csv

initial_corpora = "D:\\Mano\\_Uni\\NL\\NL year 2\\4.5 project\\corpora\\deu_news_2022_1M\\deu_news_2022_1M-words.txt"
shortnened_corpora = "D:\\Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\Output\\output-deu_news_2022_1M-words.txt"

unique_words = set()
removed_words = set()

# Open the TSV and CSV files
with open(initial_corpora, "rb") as file_in, open(shortnened_corpora, "w", newline="", encoding="utf-8") as file_out:
    tsv_reader = csv.reader((line.decode("utf-8", errors="ignore") for line in file_in), delimiter="\t")  # Create a TSV reader, ignoring decoding errors

    csv_writer = csv.writer(file_out)  # Create a CSV writer
    for row in tsv_reader:
        if len(row) >= 3:
            word = row[1].lower()  # Convert the word to lowercase
            if word in unique_words:
                removed_words.add(word)  # Add the lowercase word to the set of duplicate words
            else:
                unique_words.add(word)  # Add the lowercase word to the set of unique words
                csv_writer.writerow([word])  # Write the lowercase word to the CSV file
            
# Write the duplicate words to a separate file
removed_duplicates = "D:\\Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\Output\\removed_words-output-deu_news_2022_1M-words.txt"
with open(removed_duplicates, "w", encoding="utf-8") as file_duplicate:
    for word in removed_words:
        file_duplicate.write(word + "\n")