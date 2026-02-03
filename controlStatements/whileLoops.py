# while loops in python
# Basic while loop: count from 1 to 5
i = 1
while i <= 5:
    print("Counting:", i)
    i += 1

print("---")

# Using break: stop loop when a condition is met
n = 10
while True:
    print("n =", n)
    if n == 13:
        print("Breaking out of loop")
        break
    n += 1

print("---")

# Using continue: skip even numbers
x = 0
while x < 6:
    x += 1
    if x % 2 == 0:
        continue  # skip even numbers
    print("Odd number:", x)

print("---")

# Using else with while: runs if loop wasn't broken
count = 3
while count > 0:
    print("Countdown:", count)
    count -= 1
else:
    print("Loop finished without break")

print("---")

# Example: input validation with while
# (commented out to avoid blocking script)
# user_input = ""
# while user_input != "yes":
#     user_input = input("Type 'yes' to continue: ")
# print("Thank you!")

# Infinite loop example (use with caution)
# while True:
#     print("This would run forever unless broken")
#     break  # prevent actual infinite loop in example