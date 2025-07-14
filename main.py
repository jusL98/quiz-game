import time

def load_quiz_data(filename):
    questions = []
    options = []
    answers = []
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    for i in range(0, len(lines), 7):
        questions.append(lines[i])
        options.append(tuple(lines[i+1:i+6]))
        answers.append(lines[i+6].upper())
    return questions, options, answers

# Load quiz data from file
questions, options, answers = load_quiz_data('quiz_data.txt')
guesses = []
score = 0

# Questions, options and guesses loop
for question_num, question in enumerate(questions, 1):
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

# Prints quiz results and evaluates correct answers
print('\n-----------------------')
time.sleep(0.5)
print('Evaluating...')
for i in range(3,0,-1):
    time.sleep(1)
    print(i)
print()
time.sleep(1)

for i in range(len(questions)):
    if guesses[i] == answers[i]:
        correct_index = ord(answers[i]) - ord('A')
        print(f'✓ - Question {i+1} was correct! You chose ({options[i][correct_index]}).')
        score+=1
    else:
        correct_index = ord(answers[i]) - ord('A')
        print(f'✖ - Question {i+1} was incorrect! The answer was ({options[i][correct_index]}).')

# Prints final score
time.sleep(1)
print(f'\nYour score is {score}/{len(questions)}. {(score/len(questions)*100)}%')
