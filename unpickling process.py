import pickle

initial_pickle = "D:\\Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\_pickles\\word_german.pkl"
unpickled_file = "D:\\Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\Output\\unpickled_german.py"
re_pickle = "D:\\Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\Output\\repickled_german.pkl"
change_log_file = "D:\\Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\Output\\change_log_german.txt"

def write_change_log(original_value, modified_value, replaced_substrings):
    with open(change_log_file, 'a', encoding='utf-8') as file:
        file.write("before:\n")
        file.write(original_value + '\n')
        file.write("after:\n")
        file.write(modified_value + '\n')
        file.write("stuff changed:\n")
        for substring in replaced_substrings:
            file.write(substring + '\n')
        file.write("------------\n")

def processing_function(value):
    new_value = []
    for item in value:
        if '\n' in item:
            words = item.split('\n')
            for word in words:
                replaced_substrings = []
                processed_word = word.replace('fig.', '')
                if processed_word != word:
                    replaced_substrings.append('fig.')
                processed_word = processed_word.replace(',', '')
                if processed_word != word:
                    replaced_substrings.append(',')
                processed_word = processed_word.replace('abwertend', '')
                if processed_word != word:
                    replaced_substrings.append('abwertend')
                processed_word = processed_word.strip()
                if processed_word:
                    new_value.append(processed_word.lower())
                    # Write the changes made with .split to the change log
                    write_change_log(item, processed_word, replaced_substrings)
        else:
            replaced_substrings = []
            processed_item = item.replace('fig.', '')
            if processed_item != item:
                replaced_substrings.append('fig.')
            processed_item = processed_item.replace(',', '')
            if processed_item != item:
                replaced_substrings.append(',')
            processed_item = processed_item.replace('abwertend', '')
            if processed_item != item:
                replaced_substrings.append('abwertend')
            processed_item = processed_item.strip()
            if processed_item:
                new_value.append(processed_item.lower())
    return new_value

def unpickling_the_snake(dictionary, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("scraped_german = {\n")
        for key in sorted(dictionary):
            value = dictionary[key]
            if value is not None:
                value = processing_function(value)
            file.write(f"    {repr(key)}: {repr(value)},\n")
        file.write("}")
    with open(re_pickle, 'wb') as output_file1:
        pickle.dump(dictionary, output_file1)

german_dictionary = {}

with open(initial_pickle, 'rb') as file:
    scraped_german = pickle.load(file)

unpickling_the_snake(scraped_german, unpickled_file)
