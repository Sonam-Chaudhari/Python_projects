# Step 1: Importing the required library
from spellchecker import SpellChecker

# Step 2: Creating the app class
class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self, text):
        words = text.split()  # Splitting the text into a list of words
        corrected_words = []  # Initialize the list to store corrected words

        for word in words:
            # Get the corrected word
            corrected_word = self.spell.correction(word)
            
            if corrected_word != word.lower():  # Check if the word was corrected
                print(f'Correcting "{word}" to "{corrected_word}"')

            # Append the corrected word to the list
            corrected_words.append(corrected_word)

        # Step 4: Joining the list of corrected words into a single string and returning it
        return ' '.join(corrected_words)  # Adding a space between corrected words
    
    # Step 5: Running the app, where the user will provide text, and the text gets corrected
    def run(self):
        print("\n---Spell Checker---")

        while True:
            text = input('Enter text to check (or type "exit" to quit):')

            if text.lower() == 'exit':
                print('Closing the program...')
                break
            
            corrected_text = self.correct_text(text)
            print(f'Corrected Text: {corrected_text}')

# Step 6: Running the main program
if __name__ == "__main__":
    SpellCheckerApp().run()
