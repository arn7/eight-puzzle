#Ashley Naratadam
import heapq

class PQ: # class for a priority queue; used in Uniform-Cost , Best First, A*

    def __init__(self):
        self.content = []

    def insert(self, priority, node): # basic insert for queue; accepts tuples that contain a priority and a node
        heapq.heappush(self.content, (priority, node))

    def insert2(self, priority, node): # insert used if the node's state already exists in frontier
        for item in self.content:
            if node.state == item[1].state:
                if priority < item[0]:
                    # checks if the item to be inserted has a lower cost/priority than the other node
                    self.content.pop(self.content.index(item))
                    # if the node already in the PQ has a higher priority, it is removed
                    self.insert(priority, node) # the new tuple, with lower priority, is inserted
                else:
                    pass
    def pop(self): # pops tuple with lowest priority
        return heapq.heappop(self.content)

    def isEmpty(self): # returns true if PQ is empty
        return len(self.content) == 0

    def inQueue(self, node): # returns true if a node's state is already in the PQ
        return node in (item[1] for item in self.content)

    def size(self): # returns size of PQ
        return len(self.content)

    def __iter__(self):
        return iter(self.content)

















