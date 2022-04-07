from translate import Translator

translator = Translator(to_lang="mn")
try:
    with open('./text.txt', mode:'r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
except FileNotFoundError as err:
    print('File path inccorrect')