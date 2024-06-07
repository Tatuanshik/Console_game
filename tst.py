import random
from colorama import Fore,Back,Style,init

init(autoreset=True)

class Word:
    FILENAME = 'words-2.txt'

    def __init__(self):
        self.word = self.load_words()


    def load_words(self):
        with open(self.FILENAME, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f]


    def create_random(self):
        return random.choice(self.word)


    def idea(self, secret_w, guessed_w ):
        correct = []
        for i in range(5):
            if guessed_w[i] == secret_w[i]:
                correct.append(Fore.YELLOW + guessed_w[i] + Style.RESET_ALL)
            elif guessed_w[i] in secret_w:
                correct.append(Fore.LIGHTRED_EX + guessed_w[i] + Style.RESET_ALL)
            else:
                correct.append(guessed_w[i])
        return ''.join(correct)

    def play_game(self):
        secret_word = self.create_random()
        attempts = 6

        while attempts > 0:
            guess = input('Введите слово из 5 букв: ').strip().lower()
            if len(guess) > 5 or len(guess) < 5:
                print("Слово должно состоять из 5 букв")
                break
            feedback = self.idea(secret_word, guess)
            print(feedback)
            if guess == secret_word:
                print('Поздравляю! Слово отгадано!')
                break

            attempts -= 1
        if attempts == 0:
            print(f'К сожалению, вы использовали все попытки. Загаданное слово: {secret_word}')

a = Word()
a.play_game()