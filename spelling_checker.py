#step1 importing the required library
from spellchecker import SpellChecker
from indexer import DictionaryIndex
#step2 creating the app class
class SpellCheckerApp:
    def __init__(self):
        self.spell =SpellChecker()

    def correct_text(self,text):
        words =text.split() #hello world ['hello','word']
        corrected_words =[]

        for word in words:
            corrected_words =self.spell.correction(word)
            if corrected_words != word.lower():
                print(f'Correcting"{word}" to "{corrected_words}"')
                corrected_words.append(corrected_words)

        #step 4 returning the corrected text
        return ''.join(corrected_words)
    
     #step5 running the app where user will be providing the text and text get corrected and this will be put in loop where until user quits it will keep running
     # Function in loop ( User --> Text --> Input)
    def run(self):
        print("\n---Spell Checker---")

        while True:
            text = input('Enter text to check (or type "exit" to quit):')

            if text.lower() =='exit':
                print('Clossing the program......')
                break
            corrected_text =self.correct_text(text)
            print(f'Corrected Text :{corrected_text}')

#step six running the main program
if __name__ == "__main__":
    SpellCheckerApp().run()