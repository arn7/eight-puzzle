# Ashley Naratadam
from EightPuzzle.Search import *

difficulty = raw_input("Enter difficulty level for puzzle: easy, medium or hard: ")

easy = Node([1, 3, 4, 8, 6, 2, 7, 0, 5])
medium = Node([2, 8, 1, 0, 4, 3, 7, 6, 5])
hard = Node([5, 6, 7, 4, 0, 8, 3, 2, 1])

if difficulty == "easy":
    print "Breadth-first Search: "
    for item in bfs(easy):
        print item

    print "Uniform-Cost Search: "
    for item in uCost(easy):
        print item

    print "Best-first Search: "
    for item in bestFirst(easy):
        print item

    print "A*1: "
    for item in astar(easy):
        print item

    print "A*2: "
    for item in astar2(easy):
        print item

elif difficulty == "medium":
    print "Breadth-first Search: "
    for item in bfs(medium):
        print item

    print "Uniform-Cost Search: "
    for item in uCost(medium):
        print item

    print "Best-first Search: "
    for item in bestFirst(medium):
        print item

    print "A*1: "
    for item in astar(medium):
        print item

    print "A*2: "
    for item in astar2(medium):
        print item

elif difficulty == "hard":
    print "Best-First Search: "
    for item in bestFirst(hard):
        print item

else:
    print "invalid difficulty level"




# for item in dfs(easy): # takes too long (9 mins)
#     print item
#
