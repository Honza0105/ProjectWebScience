import pickle

initial_pickle = "D:\\_Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\_pickles\\word_german.pkl"
unpickled_file = "D:\\_Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\Output\\unpickled_german.py"
re_pickle = "D:\\_Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\Output\\repickled_german.pkl"
change_log_file = "D:\\_Mano\\Projektėliai\\GitHub\\ProjectWebScience\\Files for PWS\\Output\\change_log_german.txt"

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
replacements = [', abwertend',          #works, don't touch
                'engl.',
                'fig.',
                'NS-Jargon',
                '\', \'Unterbegriffe',  #works, don't touch
                '\'Unterbegriffe\', ',  #works, don't touch
                'österr.',
                'bayr.',
                'schweiz.',
                ', salopp',             #works, don't touch
                ' ruhrdt.',
                'auch ironisch',
                'auch figurativ',
                ', ironisch',
                ', berlinerisch',
                '[Hinweis: weitere Informationen erhalten Sie durch Ausklappen des Eintrages]',
                ' geh.',
                ', sehr',
                'franz.',
                ' norddeutsch',
                ' Hauptform',
                ' ugs.',
                ', Jargon',
                'Assoziationen	',      #works, don't touch, it has tab you see
                ' scherzhaft-ironisch',
                ', veraltet',
                ', journalistisch',
                ', politisch',
                ', Spruch',
                ' sprichwörtlich',      #works, don't touch
                ' Modewort',
                ' Amtsdeutsch',
                ', juristisch',
                ' kölsch',
                ', floskelhaft',
                ' regional',
                ' lat.',
                ', rheinisch',
                ', jugendsprachlich',
                ', ironisierend',
                ', bairisch',
                ' negativ',
                ' positiv',
                ', sehr selten',
                'fachspr.',
                ', scherzhaft',
                ', rheinisch',
                ', scherzhaft-ironisch',
                'süddt.',
                ', variabel',
                ', Kindersprache',
                ', verhüllend',
                ', selten',
                ', Babysprache',
                ', Redensart',
                'ostösterreichisch',
                ', Verballhornung',
                ', militärisch',
                ', amtsdeutsch',
                ', regional',
                ', emotional',
                ', medizinisch',
                ', griechisch',
                ', biologisch',
                ', sprichwörtlich',
                ' Anglizismus',
                ', altertümelnd',
                ' Sprichwort',
                ', übertreibend',
                ' saarländisch',
                'weibl.',
                ', aggressiv',
                ', Zitat',
                ', sarkastisch',
                ' biblisch',
                ' plattdeutsch',
                ' werbesprachlich',
                ' bildungssprachlich',
                ' technisch',
                ' literarisch',
                ', Salzburg',
                ', formelhaft',
                ' pfälzisch',
                ' schwäbisch',
                ' ostfriesisch',
                ' bundesdeutsch',
                ', Kunst',
                ' kaufmännisch',
                ', modewort',
                ', kurzform',
                ' wienerisch',
                ' südösterreichisch',
                ', Neologismus',
                ', IT-Technik',
                ', religiös',
                ' mathematisch',
                ' kölsch',
                ' moselfränkisch',
                ' Jägersprache',
                ' bairisch',
                ' juristisch',
                'männl.',
                ' südtirolerisch',
                ' walliserisch',
                ' dichterisch',
                ', Philosophie',
                'Scheinanglizismus',
                'Markenname',
                'ital.',
                ', kommentierend',
                ' euphemistisch',
                ' seemännisch',
                ' Verstärkung',
                ' hessisch',
                ' psychologisch',
                ' mediensprachlich',
                ' mitteldeutsch',
                ', Plural',
                ', selten',
                ' Schimpfwort',
                ' Abkürzung',
                ' sächsisch',
                ' alemannisch',
                ' sexualisiert',
                ' Papierdeutsch',
                ' westfälisch',
                'alte Schreibung bis 2017',
                ' kärntnerisch',
                ' Schlagwort',
                ' vorarlbergerisch',
                ' französierend',
                ' gendergerecht',
                ' derb',
                ' veraltend',
                'bayr.',
                ' historisch',
                ' denglisch',
                ' Ostdeutsch',
                'fränk.',
                'vulg.',
                ' , ,',                 #clean up crew
                ' ,, '                  #clean up crew
                ]

def process_word(word):
    replaced_substrings = []
    for substring in replacements:
        if substring in word:
            word = word.replace(substring, '')
            replaced_substrings.append(substring)
    processed_word = word.lower().strip()
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
                processed_item = processed_item.rstrip(', ')
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
    with open(re_pickle, 'wb') as gabijabuvocia:
        pickle.dump(dictionary, gabijabuvocia)

german_dictionary = {}

with open(initial_pickle, 'rb') as file:
    scraped_german = pickle.load(file)

unpickling_the_snake(scraped_german, unpickled_file)
