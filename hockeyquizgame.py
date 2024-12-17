"""
This program will create a hockey quiz game.
"""

# Imports -----------------------------
import time

# Variables ---------------------------
questions = ('How many periods in a hockey game? ',
             'How many players do you start the game with? ',
             'What number is Connor McDavid? ',
             'Who is the coach of the New Jersey Devils? ',
             'Which NHL team has a mask as part of their logo? '
             )
options = (('A. 1', 'B. 2','C. 3','D. 4','E. 5'),
           ('A. 2', 'B. 7','C. 3','D. 4','E. 6'),
           ('A. 98', 'B. 99','C. 97','D. 79','E. 89'),
           ('A. Sheldon Keefe', 'B. Craig Berube','C. Paul Maurice','D. Jim Montgomery','E. Kyle Dubas'),
           ('A. New Jersey Devils', 'B. Anaheim Ducks','C. Toronto Maple Leafs','D. Montreal Canadians','E. Detroit Red Wings')
           )
answers = (('C', 2),
           ('E', 4),
           ('C', 2),
           ('A', 0),
           ('B', 1)
        )
guesses = []
question_num = 0
score = 0

# Code --------------------------------
# Questions/Options/Guesses
for question in questions:
    question_num = question_num + 1
    print(f'\n{question_num}. {question}')
    
    for i in range(5):
        print(f'-----{options[question_num-1][i]}')
    while True:
        guess = (input('Your guess: ')).upper()
        if guess in ('A','B','C','D','E'):
            break
        else:
            print('Invalid entry please type (A/B/C/D/E).')

    
    guesses.append(guess)

# Answers
print('\n-----------------------')
time.sleep(0.5)
print('Evaluating...')
for i in range(3,0,-1):
    time.sleep(1)
    print(i)
print()
time.sleep(1)

question_num = 0
for i in range(5):
    question_num += 1
    if guesses[i] == answers[i][0]:
        print(f'✓ - Question {question_num} was correct! You chose ({options[question_num-1][answers[i][1]]}).')
        score+=1
    else:
        print(f'X - Question {question_num} was incorrect! The answer was ({options[question_num-1][answers[i][1]]}).')

time.sleep(1)

print(f'\nYour score is {score}/5. {(score/5*100)}%')
