####### ----- USER ----- #######
##### Data structures (Dictionaries, Lists)
entities = {
    "m": "man",
    "w": "wolf",
    "ch": "chicken",
    "co": "corn"
}

loseConditions = {
    1: sorted(["wolf", "chicken"]),
    2: sorted(["chicken", "corn"]),
    3: sorted(["wolf", "chicken", "corn"])
}

northList = [entities["m"], entities["w"], entities["ch"], entities["co"]]
southList = []


####### Functions
def choiceVerifier(userChoice):
    '''if (onNorth == True and onSouth == False):
        if userChoice == "m":
            print()
            print("You can't enter [m] when you're on NORTH.")
            return False '''
    for chars in entities:
        if userChoice == chars:
            return True
    return False

def listPrinter():
    print("———————————————————————")
    print()

    print(f"Current state of NORTH: ", end="")
    for x in northList:
        print(x, end=" ")

    print()

    print(f"Current state of SOUTH: ", end="")
    for y in southList:
        print(y, end=" ")
    
    print()
    print()
    print("———————————————————————") 

def gameOver(north, south, loseCons):
    for i in loseCons:
        if((sorted(north) == loseCons[i]) or (sorted(south) == loseCons[i])):
            return True
    return False

def winner():
    if((len(northList) == 0) and (len(southList) == 4)):
        return True
    else:
        return False


####### User Algorithm
def gameAlgorithm():
    stepsCount = 0  # Steps counter
    # Initial position of the man
    onNorth = True
    onSouth = False
    while (gameOver(northList, southList, loseConditions) == False):
        listPrinter()
        
        while True:
            userChoice = str(input("""
                Press [w] for Wolf
                Press [ch] for Chicken
                Press [co] for Corn
                Press [m] for Man

                Enter your choice: """))
            if (choiceVerifier(userChoice) == True):
                break
            else:
                print()
                print("You entered an invalid input. Please try again.")
                print()

        # Position Mover
        if onNorth == True:
            if userChoice == "m":
                southList.append(entities[userChoice])
                northList.remove(entities[userChoice])
            else:
                southList.append(entities[userChoice])
                southList.append(entities["m"])

                northList.remove(entities[userChoice])
                northList.remove(entities["m"])

            stepsCount+=1   # Add 1 step
            # Change position
            onNorth = False
            onSouth = True
    
        elif onSouth == True:
            if userChoice == "m":
                northList.append(entities[userChoice])
                southList.remove(entities[userChoice])
            else:
                northList.append(entities[userChoice])
                northList.append(entities["m"])

                southList.remove(entities[userChoice])
                southList.remove(entities["m"])

            stepsCount+=1   # Add 1 step
            # Change position
            onNorth = True
            onSouth = False

        if (winner() == True):
            listPrinter()
            print("Congratulations! You successfully crossed the river!")
            print(f"The number of steps you took: {stepsCount}")
            break
    
    if (gameOver(northList, southList, loseConditions) == True):
        listPrinter()
        print("Game over. You lose.")

# Function call
gameAlgorithm()



####### ----- COMPUTER SOLUTION ----- #######
print()
print("Simulating the most efficient algorithm using Breadth-First Search (BFS)")
print()
##### Import deque (double-ended queue)
from collections import deque

##### Data structures (Dictionaries)
initialState = {
    'man': 'north',
    'wolf': 'north',
    'chicken': 'north',
    'corn': 'north'
}

goalState = {
    'man': 'south',
    'wolf': 'south',
    'chicken': 'south',
    'corn': 'south'
}

validMoves = [
    {'man': 'south', 'chicken': 'south'},
    {'man': 'north', 'wolf': 'north', 'chicken': 'south'},
    {'man': 'south', 'wolf': 'south', 'chicken': 'south'},
    {'man': 'north', 'wolf': 'south', 'chicken': 'north'},
    {'man': 'south', 'wolf': 'south', 'corn': 'south'},
    {'man': 'north', 'wolf': 'south', 'chicken': 'north', 'corn': 'south'}
]

# Defining the function of the Breadth-First Searach (BFS) Algorithm 
def bfs(initial, goal):
    stepCount = 0
    # Initialize a deque
    queue = deque()
    queue.append(initial)
    visited = set()
    visited.add(tuple(initial.items()))
    while queue:
        state = queue.popleft()
        # Print the initial state
        if state == initialState:
            print(f"Initial State (Starting Place): {state}")

        # Print every step
        elif state != initialState:
            stepCount += 1
            print(f"Step {stepCount}: {state}")

        # Return the step count and the state if the solution (the state is equal to the goal) is met
        if state == goal:
            return stepCount, state
        for move in validMoves:
            newState = state.copy()
            newState.update(move)
            if isValid(newState) and tuple(newState.items()) not in visited:
                queue.append(newState)
                visited.add(tuple(newState.items()))

    # Return 0 and None if there are no solutions found
    return 0, None

# Define whether the state is valid or not
def isValid(state):
    if state['wolf'] == state['chicken'] and state['man'] != state['wolf']:
        return False
    elif state['chicken'] == state['corn'] and state['man'] != state['chicken']:
        return False
    elif state['wolf'] == state['chicken'] == state['corn'] and state['man'] != state['wolf']:
        return False
    return True

# Call the BFS function and print the result
stepCount, result = bfs(initialState, goalState)
if result:
    print()
    print('Solution found:', result)
    print(f"Number of steps it took: {stepCount}")
else:
    print('No solution found')