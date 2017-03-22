

goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]

class Node:
    def __init__(self, state, cost=0, parent=None, action=None, depth=0): # Node constructor
        self. state = state  # arrangement of numbers in puzzle
        self.parent = parent
        self.action = action  # the move performed on the parent that resulted in this node: up, down, left, or right
        self.depth = depth
        self.cost = cost # total cost from initial to current node

    def __eq__(self, other): # checks equality between two nodes
        return self.state == other.state

    def __str__(self): # string representation of Node
        return str(self.state) + " " + str(self.action) + " cost: " + str(self.cost) + " depth: " + str(self.depth)


    def misplacedTiles (self): # returns number of tiles that are out of place in a node's state
        count = 0
        for i in range(0, len(self.state)):
            if self.state[i] != 0 and self.state[i] != goal[i]:
                count += 1
        return count

    def manhattanDistance(self): # returns sum of the Manhattan distances for the tiles in a node
        s = self.state[:]
        sum = 0
        for i in range(1, 9):
            # add abs. value of distances of tiles from goal positions
            sum += (abs((s.index(i)//3) - (goal.index(i)//3)) + abs((s.index(i)%3) - (goal.index(i)%3)))
        return sum


    def expand(self): # returns a list with the node's successors after expansion
        blank = self.state.index(0) # stores index of blank space
        successors = [] # list with successors
        d = self.depth
        c = self.cost
        if blank > 2: #to move the space up
            successor = self.state[:]
            successor[blank], successor[blank - 3] = successor[blank - 3], 0
            successors.append(Node(successor, c + successor[blank], self, "up   ", d+1))
        if blank < 6: #to move the space down
            successor = self.state[:]
            successor[blank], successor[blank + 3] = successor[blank + 3], 0
            successors.append(Node(successor, c + successor[blank], self, "down ", d+1))
        if blank not in [0, 3, 6]: # to move the space to the left
            successor = self.state[:]
            successor[blank], successor[blank - 1] = successor[blank - 1], 0
            successors.append(Node(successor, c + successor[blank], self, "left ", d+1))
        if blank not in [2, 5, 8]: #to move the space to the right
            successor = self.state[:]
            successor[blank], successor[blank + 1] = successor[blank + 1], 0
            successors.append(Node(successor, c + successor[blank], self, "right", d+1))
        return successors





