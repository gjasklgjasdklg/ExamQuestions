import random as rand

num_correct = 0
guesses_left = 11
for _ in range(11):
    code = rand.randrange(10, 100)
    guess = int(input("Guess a two digit whole number: "))
    guesses_left -= 1
    if guess == code:
        num_correct += 1
        print("Correct!")
    elif guess != code:
        print("Wrong, try again!")
    print(str(guesses_left) + " guesses left!")

print("No more guesses")
print("Your score was " + str(num_correct))
