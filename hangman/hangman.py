import random
words_list = ['dereng', 'boi', 'kekw', 'easter']
a = random.choice(words_list)

print(f'the solution is {a}')

display = []
for _ in range(len(a)):
    display += "_"
print(display)

end_of_game = False

while not end_of_game: 
    guess = input('Enter the correct letter in the word: ').lower()
    
    for position in range(len(a)):
        letter = a[position]
        if letter == guess:
            display[position] = letter

    print(f"{' '.join(display)}")

    if '_' not in display:
        end_of_game = True
        print('you win')
