"""Today I will be making the game Hangman."""
import random

print(""" 
 _                                            
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       """)  # Art from https://ascii.co.uk/art/hangman

stages = ["""
  +---+
  |   |
      |
      |
      |
      |
=========""", """
  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
 +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
 +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]
# Art from https://codegolf.stackexchange.com/questions/135936/ascii-hangman-in-progress

word_list = ['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra',
             'cougar', 'coyote', 'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle', 'ferret', 'fox',
             'frog', 'goat', 'goose', 'hawk', 'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose'
             'mouse', 'mule', 'newt', 'otter', 'owl', 'panda', 'parrot', 'pigeon', 'python',
             'rabbit', 'ram', 'rat', 'raven', 'rhino', 'salmon', 'seal', 'shark', 'sheep', 'skunk',
             'sloth', 'snake', 'spider', 'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey',
             'turtle', 'weasel', 'whale', 'wolf', 'wombat', 'zebra']

while True:
    word = random.choice(word_list)
    print('The word is an animal.')
    gaps = []
    for num_gaps in range(0, len(word)):
        gaps += '_'

    print(stages[0])

    print(f'This word has {len(gaps)} letters in it.')
    stage_num = 1
    chosen = []
    while '_' in gaps:
        user_input = input('Guess a letter: \n').lower()
        while user_input in chosen:
            print('You have already guessed this letter. Guess again.')
            user_input = input('Guess a letter: \n').lower()
        chosen.append(user_input)
        num = 0
        for j in range(len(word)):
            if word[j] == user_input:
                gaps[j] = word[j]
                num += 1
        if stage_num == 6 and num == 0:
            print(stages[stage_num])
            print('Sorry, you lost the game.')
            print(f'The word was {word}')
            break
        if num == 0:
            print('You guessed wrong')
            print(stages[stage_num])
            stage_num += 1
        elif num == 1:
            print('You Guessed 1 digit')
            print(stages[stage_num - 1])
        else:
            print(f'You guessed {num} digits right.')
            print(stages[stage_num - 1])

        print(gaps)
        if '_' not in gaps:
            print("Congratulations! You won the game.")

    play_again = input('Play again? Y or N: ')
    if play_again.lower() != 'y':
        print('Thank you for playing.')
        break
