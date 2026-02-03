# 4.4 break and continue Statements, and else Clauses on Loops . . . . . . . . . . . . . . . . . . 21
# thebreak and continue statements are used to alter the flow of loops in Python. The break statement is used to exit a loop prematurely, while the continue statement is used to skip the current iteration and move to the next one. Additionally, Python allows the use of else clauses with loops, which execute when the loop completes normally (i.e., not terminated by a break statement).


# break statement
for i in range(10):
    if i == 5:
        break  # exit the loop when i is 5
    print(i)

# continue statement
for i in range(10):
    if i % 2 == 0:
        continue  # skip even numbers
    print(i)
# else clause with loop
for i in range(5):
    print(i)
else:
    print("Loop completed without break")