import random
print("number guessing game")

number = random.randint(1,9)

chances = 0
print('guess a numer between one and nine')

while chances < 5:
    guess = int(input('enter your guess'))
    if guess == number:
        print('congratulation YOU WON !!')
        break
    elif guess < number:
        print('guees is low ',guess)
    else:
        print('guess is high ',guess)

    chances += 1
    
if not chances < 5:
    print('YOU LOSE !!! the number is  ',number)


                