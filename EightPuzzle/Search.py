
from EightPuzzle.Node import Node
from EightPuzzle.PriorityQueue import PQ

goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]

def bfs(root):  # breadth first search
    frontier = []   # nodes available for expansion
    explored = []   # expanded nodes
    time = 0    # number of nodes popped
    maxSize = 0 # will hold the queue size at its largest
    if goalTest(root):  # checks if root has the goal state
        return solution(root, time, maxSize)
    frontier.append(root)
    while len(frontier) != 0:
        # goalTest and expand nodes on frontier until solution is found or no states remain for expansion
        if maxSize < len(frontier):
            maxSize = len(frontier)
        current = frontier.pop(0)   # pop off and set current node to the FIRST node in frontier
        time += 1
        explored.append(current)    # add current node to the explored list
        for move in current.expand():   # current node's successors
            if (move not in frontier) and (move not in explored):
                # only continue with nodes whose states have not been seen before
                if goalTest(move):
                    return solution(move, time, maxSize)
                frontier.append(move) # add successors to frontier
    return "failure"

def dfs(root):  # depth first search
    time = 0
    maxSize = 0
    if goalTest(root):  # test root for goal state
        return solution(root, time, maxSize)
    frontier = []   # nodes available for expansion
    explored = []   # nodes already expanded
    frontier.append(root)
    while frontier != []:
        # goalTest and expand nodes on frontier until solution is found or no states remain for expansion
        if maxSize < len(frontier):
            maxSize = len(frontier)
        current = frontier.pop() # pops nodes from END (LIFO)
        time += 1
        explored.append(current.state)  # add expanded nodes to explored
        moves = current.expand()    # list of successor/child nodes
        for move in moves:
            if (move not in frontier) and (move.state not in explored):
                # only continue with nodes whose states have not been seen before
                if goalTest(move):
                    return solution(move, time, maxSize)
                frontier.append(move)

    return "failure"


def uCost(root): # uniform-cost search
    frontier = PQ() # priority queue based on cost
    explored = []
    time = 0
    maxSize = 0
    frontier.insert(root.cost, root)
    while not frontier.isEmpty():
        if maxSize < frontier.size():
            maxSize = frontier.size()
        current = frontier.pop()    # pops node with lowest cost
        time += 1
        if goalTest(current[1]):    # goalTest applies when node is selected for expansion
            return solution(current[1], time, maxSize) #return if it == goal
        explored.append(current[1]) # add current node to explored
        for move in current[1].expand():
            if(not frontier.inQueue(move)) and (move not in explored):
                frontier.insert(move.cost, move)
            elif frontier.inQueue(move):
                # if move's state is already in frontier, only keep node with lower cost
                frontier.insert2(move.cost, move)
    return "failure"

def bestFirst(root):
    # best first search
    # evaluates nodes using heuristic function f(n) = h(n) where h(n) is the no. of misplaced tiles
    frontier = PQ() # priority queue
    explored = []
    time = 0
    maxSize = 0
    frontier.insert(root.misplacedTiles(), root)    # priority based on number of misplaced tiles in node's state
    while not frontier.isEmpty():
        if maxSize < frontier.size():
            maxSize = frontier.size()
        current = frontier.pop()    # node with lowest priority value (fewest misplaced tiles) will be expanded
        time += 1
        if goalTest(current[1]): # goalTest done when node is selected for expansion
            return solution(current[1], time, maxSize)
        explored.append(current[1])
        for move in current[1].expand():
            if (not frontier.inQueue(move)) and (move not in explored): # duplicate check
                frontier.insert(move.misplacedTiles(), move)
            elif frontier.inQueue(move):
                frontier.insert2(move.misplacedTiles(), move) #if duplicate state, only keep node with lower priority
    return "failure"


def astar(root):
    # uses g(n) + h(n) to evaluate nodes; g(n) is cost to reach the node and h(n) estimates cost from node to goal
    # heuristic used is number of misplaced tiles
    frontier = PQ()
    explored =[]
    time = 0
    maxSize = 0
    frontier.insert(root.misplacedTiles()+root.cost, root)
    # priority based on g(n) + h(n) = total cost+  number of misplaced tiles
    while not frontier.isEmpty():
        if maxSize < frontier.size():
            maxSize = frontier.size()
        current = frontier.pop() # node with lowest total cost + # of misplaced tiles chosen for expansion
        time += 1
        if goalTest(current[1]): # goalTest applied to node after it is selected for expansion
            return solution(current[1], time, maxSize)
        explored.append(current[1])
        for move in current[1].expand():
            if (not frontier.inQueue(move)) and (move not in explored): # duplicate check
                frontier.insert(move.misplacedTiles()+ move.cost, move)
            elif frontier.inQueue(move):
                frontier.insert2(move.misplacedTiles()+ move.cost, move) # only keep node with lower priority
    return "failure"


def astar2(root):
    # uses g(n) + h(n) to evaluate nodes; g(n) is cost to reach the node and h(n) estimates cost from node to goal
    # heuristic used is the sum of manhattan distances (no. of squares from goal location for each tile)
    frontier = PQ()
    explored =[]
    time = 0
    maxSize = 0
    frontier.insert(root.manhattanDistance()+root.cost, root)
    # priority queue ordered by g(n) + h(n) = total cost + sum of manhattan distances
    while not frontier.isEmpty():
        if maxSize < frontier.size():
            maxSize = frontier.size()
        current = frontier.pop() # node with lowest priority value is chosen for expansion
        time += 1
        if goalTest(current[1]): # goalTest applied when node is selected for expansion
            return solution(current[1], time, maxSize)
        explored.append(current[1])
        for move in current[1].expand():
            if (not frontier.inQueue(move)) and (move not in explored): # duplicate check
                frontier.insert(move.manhattanDistance()+ move.cost, move)
            elif frontier.inQueue(move):
                frontier.insert2(move.manhattanDistance()+move.cost, move) # insert/keep node with lower priority
    return "failure"



def goalTest(node): # returns true if node's state equals goal state
    return node.state == goal

def solution(node, time, space): # returns the solution path for the search; includes # of nodes popped and queue size at its largest
    path = []
    path.append(node)
    while node.parent:
        node = node.parent
        path.append(node)
    path = path[::-1]
    path.append(str(time) + " nodes popped; " + str(space) + " nodes at largest")
    return path

