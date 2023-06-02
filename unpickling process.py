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
        if replaced_substrings:
            file.write("stuff changed:\n")
            for substring in replaced_substrings:
                changed_string = next((s for s in replacements if substring in s), None)
                if changed_string:
                    file.write("- {}\n".format(changed_string))
        file.write("------------\n")

# This is pretty funky, idk if it will actually work
replacements = [', abwertend, fig.',
                ', engl.',
                ', fig.',
                '\', \'Unterbegriffe',
                '\'Unterbegriffe\', ',
                ', österr., bayr.',
                ', schweiz.',
                ', salopp',
                ', ruhrdt.',
                ' ironisch',
                ', berlinerisch',
                '[Hinweis: weitere Informationen erhalten Sie durch Ausklappen des Eintrages]',
                'geh., ',
                ', sehr',
                ' franz.,',
                'norddeutsch',
                ', Hauptform',
                ' ugs.,',
                ' Jargon',
                'Assoziationen	',
                ' scherzhaft-ironisch',
                ', veraltet',
                ' , ,',
                ' ,, '
                ]

def process_word(word):
    processed_word = word.lower()
    replaced_substrings = []
    for substring in replacements:
        processed_word = processed_word.replace(substring, '')
        if processed_word != word.lower():
            replaced_substrings.append(substring)
    processed_word = processed_word.strip()
    return processed_word, replaced_substrings

def processing_function(value):
    new_value = []
    for item in value:
        if '\n' in item:
            words = item.split('\n')
            for word in words:
                processed_word, replaced_substrings = process_word(word)
                if processed_word:
                    new_value.append(processed_word)
                    write_change_log(word, processed_word, replaced_substrings)
        else:
            processed_item, replaced_substrings = process_word(item)
            if processed_item:
                new_value.append(processed_item)
                write_change_log(item, processed_item, replaced_substrings)
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
