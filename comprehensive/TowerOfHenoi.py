'''Implement the Tower of Hanoi Algorithm
In this lab, you will solve the mathematical puzzle known as the Tower of Hanoi. The puzzle consists of three rods and a number of disks of different diameters.

sequence of moves required to solve a 3-disks tower of Hanoi puzzle
The puzzle starts with the disks piled up on the first rod, in decreasing size, with the smallest disk on top and the largest disk on the bottom.

The goal of the Tower of Hanoi puzzle is moving all the disks to the last rod. To do that, you must follow three simple rules:

You can move only top-most disks.
You can move only one disk at a time.
You cannot place larger disks on top of smaller ones.
Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

You should have a function named hanoi_solver that takes an integer representing the total number of disks of the puzzle as the argument.
The hanoi_solver function should solve the puzzle following the given rules in 2n - 1 moves, where n is the total number of disks.
The hanoi_solver function should return a string with all the moves taken to solve the puzzle, including the starting arrangement, with each move on a new line. Rods should be represented as lists of integers, (the smallest disk is represented by the number 1) with each rod separated by a space. For example, hanoi_solver(3) should return the following:
[3, 2, 1] [] []
[3, 2] [] [1]
[3] [2] [1]
[3] [2, 1] []
[] [2, 1] [3]
[1] [2] [3]
[1] [] [3, 2]
[] [] [3, 2, 1]
Run the Tests (Ctrl + Enter)
Save your Code
Revert to Saved Code
Get Help
Tests
Waiting:1. You should have a function named hanoi_solver.
Waiting:2. Your hanoi_solver function should take a single argument.
Waiting:3. Your hanoi_solver function should return a string.
Waiting:4. hanoi_solver(2) should return [2, 1] [] []\n[2] [1] []\n[] [1] [2]\n[] [] [2, 1].
Waiting:5. hanoi_solver(3) should return [3, 2, 1] [] []\n[3, 2] [] [1]\n[3] [2] [1]\n[3] [2, 1] []\n[] [2, 1] [3]\n[1] [2] [3]\n[1] [] [3, 2]\n[] [] [3, 2, 1].
Waiting:6. hanoi_solver(4) should return [4, 3, 2, 1] [] []\n[4, 3, 2] [1] []\n[4, 3] [1] [2]\n[4, 3] [] [2, 1]\n[4] [3] [2, 1]\n[4, 1] [3] [2]\n[4, 1] [3, 2] []\n[4] [3, 2, 1] []\n[] [3, 2, 1] [4]\n[] [3, 2] [4, 1]\n[2] [3] [4, 1]\n[2, 1] [3] [4]\n[2, 1] [] [4, 3]\n[2] [1] [4, 3]\n[] [1] [4, 3, 2]\n[] [] [4, 3, 2, 1].
Waiting:7. hanoi_solver(5) should return [5, 4, 3, 2, 1] [] []\n[5, 4, 3, 2] [] [1]\n[5, 4, 3] [2] [1]\n[5, 4, 3] [2, 1] []\n[5, 4] [2, 1] [3]\n[5, 4, 1] [2] [3]\n[5, 4, 1] [] [3, 2]\n[5, 4] [] [3, 2, 1]\n[5] [4] [3, 2, 1]\n[5] [4, 1] [3, 2]\n[5, 2] [4, 1] [3]\n[5, 2, 1] [4] [3]\n[5, 2, 1] [4, 3] []\n[5, 2] [4, 3] [1]\n[5] [4, 3, 2] [1]\n[5] [4, 3, 2, 1] []\n[] [4, 3, 2, 1] [5]\n[1] [4, 3, 2] [5]\n[1] [4, 3] [5, 2]\n[] [4, 3] [5, 2, 1]\n[3] [4] [5, 2, 1]\n[3] [4, 1] [5, 2]\n[3, 2] [4, 1] [5]\n[3, 2, 1] [4] [5]\n[3, 2, 1] [] [5, 4]\n[3, 2] [] [5, 4, 1]\n[3] [2] [5, 4, 1]\n[3] [2, 1] [5, 4]\n[] [2, 1] [5, 4, 3]\n[1] [2] [5, 4, 3]\n[1] [] [5, 4, 3, 2]\n[] [] [5, 4, 3, 2, 1].
Waiting:8. hanoi_solver(n) should solve the tower of Hanoi puzzle for any positive value of n.
Waiting:9. hanoi_solver(n) should return a list of moves that solve the tower of Hanoi puzzle for n disks.'''


# Implementing the Tower of Hanoi Algorithm
# The Tower of Hanoi is a mathematical puzzle that consists of three rods and a number of disks of different sizes. The objective of the puzzle is to move all the disks from the first rod to the last rod, following these rules:
# 1. Only one disk can be moved at a time.
# 2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
# 3. A larger disk cannot be placed on top of a smaller disk.
# 4. No disk can be placed on top of an empty rod.
# Write a function hanoi_solver that takes an integer n as input and returns a list of moves that solve the Tower of Hanoi puzzle for n disks.

def hanoi_solver(n):
    # Initialize the rods: Rod A has all disks, B and C are empty
    # Disks are represented by integers, largest at the bottom (index 0)
    rods = {
        'source': list(range(n, 0, -1)),
        'auxiliary': [],
        'target': []
    }
    
    output = []

    def get_current_state():
        # Formats the current rods into the required string format
        return f"{rods['source']} {rods['auxiliary']} {rods['target']}"

    # Capture the starting arrangement
    output.append(get_current_state())

    def move_disks(disks, src, aux, tgt):
        if disks > 0:
            # Step 1: Move n-1 disks from source to auxiliary
            move_disks(disks - 1, src, tgt, aux)
            
            # Step 2: Move the actual disk from source to target
            disk = rods[src].pop()
            rods[tgt].append(disk)
            output.append(get_current_state())
            
            # Step 3: Move the n-1 disks from auxiliary to target
            move_disks(disks - 1, aux, src, tgt)

    # Start the recursive process
    move_disks(n, 'source', 'auxiliary', 'target')
    
    # Return all moves joined by newlines
    return "\n".join(output)