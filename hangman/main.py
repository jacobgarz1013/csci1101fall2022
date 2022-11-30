import re
import random

#getting the answer
pool_file=open("hangman/hangman-sample-answer-pool.txt")

pool_answers = []

pool_answer_line = pool_file.readline()

while pool_answer_line:
    pool_answers.append(pool_answer_line)

    pool_answer_line = pool_file.readline()

pool_file.close()

answer = random.choice(pool_answers)

answer = answer.upper()

#Game setup
num_of_incorrect_guesses=5

answer_guessed=[]

for current_answer_character in answer:
    if re.search("^[A-Z]$", current_answer_character):
        answer_guessed.append(False)
    else:
        answer_guessed.append(True)

#Game logic
current_incorrect_guesses=0

letter_guessed= []

while current_incorrect_guesses < num_of_incorrect_guesses and False in answer_guessed:
    #Game summary
    print(f"Number of incorrect guesses left: {num_of_incorrect_guesses-current_incorrect_guesses}")

    print("Guessed letters: ", end="")

    for current_guessed_letter in letter_guessed:
        print(current_guessed_letter, end=" ")

    print()

    #Display puzzle here
    for current_answer_index in range(len(answer)):
        if answer_guessed[current_answer_index]:
            print(answer[current_answer_index], end="")
        else:
            print("_", end="")

    print()

    #let user guess a letter
    letter= input("Enter a letter: ")

    letter=letter.upper()

    #check if user entered a vaild letter
    if re.search("^[A-Z]$", letter) and len(letter) == 1 and letter not in letter_guessed:
        current_letter_index=0

        #insert the letter in list of letter guesses (insertion sort)
        for current_letter_guessed in letter_guessed:
            if letter < current_letter_guessed:
                break
            
            current_letter_index=+1

        letter_guessed.insert(current_letter_index, letter)

        #see if letter is in the answer
        if letter in answer:
            for current_answer_index in range(len(answer)):
                if letter == answer[current_answer_index]:
                    answer_guessed[current_answer_index]=True
        else:
            current_incorrect_guesses +=1

#post-game summary
if current_incorrect_guesses < num_of_incorrect_guesses:
    print("Congratulations, you won!")
else:
    print(f"Sorry, you lost. The answer was {answer}")