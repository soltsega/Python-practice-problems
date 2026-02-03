# random library is used when we want to generatea random nubmer from

import random

random_number = random.randint(1, 100)
print(random_number)

# this will generate a random number between 1 and 100
# other method of generating random number 

random_number = random.random()  # this is  used to generate a random number between 0 and 1
print(random_number)

# 3. Generate a random number between 1 and 10
random_number = random.randint(1, 10)
print(random_number)


# 4. to pick random item from a collection/ list, sets, tuples, or dictionaries
lists = [1, 2, 3, 4, 5]
rand_item = random.choice(lists)

sets  = (1,3,4,6,6)
rand_item = random.choice(sets)

tuples = (1,2,3,4,5)
rand_item = random.choice(tuples)

dictionaries = {"name": "solomon", "age": 12}
rand_item = random.choice(list(dictionaries.keys()))  # this will output: 
print(rand_item)
rand_item = random.choice(list(dictionaries.values()))  # this will output: 
print(rand_item)

rand_item = random.choice(list(dictionaries.items()))  # this will output: 
print(rand_item)


# let's play cards: the participant will have three chances to guess the card
cards = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
random.shuffle(cards) # to shuffle the cards
print(cards)
print(f"The card is {random.choice(cards)}")  # this will output: print(random.choice(cards))

# number guessing game: the participant will have three chances to guess the number
lowest = int(input("Enter the lowest number: "))
highest = int(input("Enter the highest number: "))
secret_num = random.uniform(lowest,highest)

count = 0
guess = 0
while guess != secret_num and count < 3:
    guess = int(input("Enter your guess: "))
    if guess < secret_num:
        print("Too low")
    else:
        print("Too high")
    count += 1

    if guess == secret_num:
        print("You win")
    else:
        print("You lose")
print(f"The secret number is {secret_num}")