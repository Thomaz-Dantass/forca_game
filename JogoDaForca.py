import tkinter as tk
import random

champions = ['Akali', 'Aurelion Sol', 'Diana', 'Fizz', 'Garen', 'Kha\'Zix', 'Leona', 'Riven', 'Syndra', 'Viktor']

word = random.choice(champions)

lives = 6
correct_letters = []
incorrect_letters = []

def check_letter():
    global lives, correct_letters, incorrect_letters
    letter = letter_entry.get().lower()
    if letter in word.lower():
        if letter not in correct_letters:
            correct_letters.append(letter)
            update_word()
        else:
            feedback_label.configure(text='Você já usou essa letra.')
    else:
        if letter not in incorrect_letters:
            incorrect_letters.append(letter)
            update_lives()
        else:
            feedback_label.configure(text='Você já usou essa letra.')

def update_word():
    displayed_word = ''
    for letter in word.lower():
        if letter in correct_letters:
            displayed_word += letter
        else:
            displayed_word += '-'
    word_label.configure(text=displayed_word)
    check_win()

def update_lives():
    global lives
    lives -= 1
    lives_label.configure(text=f'Vidas: {lives}')
    if lives == 0:
        feedback_label.configure(text=f'Você perdeu! A palavra era {word}.')
        letter_entry.configure(state='disabled')

def check_win():
    global lives
    if set(word.lower()) == set(correct_letters):
        feedback_label.configure(text='Você ganhou!')
        letter_entry.configure(state='disabled')
        lives = 0
        lives_label.configure(text=f'Vidas: {lives}')

window = tk.Tk()
window.title('Jogo da forca')
window.geometry('260x260')

word_label = tk.Label(window, text='-' * len(word))
word_label.pack()

letter_entry = tk.Entry(window)
letter_entry.pack()

submit_button = tk.Button(window, text='Adivinhar', command=check_letter)
submit_button.pack()

lives_label = tk.Label(window, text=f'Vidas: {lives}')
lives_label.pack()

feedback_label = tk.Label(window, text='')
feedback_label.pack()

window.mainloop()

