# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    
    "*** YOUR CODE HERE ***"
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    print "HELLO"

    problem.getStartState() gets the starting node. 
    problem.isGoalState(node) returns true if this is the goal/end and false if it isnt
    problem.getSuccessors(node) returns the node's successors, being successor[0] the adjacent node,
    successor[1] the edge aka path from the current node to the adjacent node, 
    and successor[2] being the cost.
    """

    "*** YOUR CODE HERE ***"

    unvisited = util.Stack()
    edgePaths = util.Stack()
    visited = []
    path = []
    start = problem.getStartState()
    currentNode = problem.getStartState()

    if problem.isGoalState(start):
        return []

    unvisited.push(start)
    while not unvisited.isEmpty():

        if problem.isGoalState(currentNode):
            return path
        
        if currentNode not in visited:
            visited.append(currentNode)
            successors = problem.getSuccessors(currentNode)

            for successor in successors:
                unvisited.push(successor[0])
                edgePaths.push(path + [successor[1]])
                
        currentNode = unvisited.pop()
        path = edgePaths.pop()

    return path



def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"

    unvisited = util.Queue()
    unvisited.push((problem.getStartState(), []))
    visited = []
    while not unvisited.isEmpty():
        current = unvisited.pop()
        currentState = current[0]
        if currentState not in visited:
            visited.append(currentState)
            if problem.isGoalState(currentState):
                return current[1]
            for each in problem.getSuccessors(currentState):
                if each[0] not in visited:
                    unvisited.push((each[0], current[1] + [each[1]]))
    # unvisited = util.Queue()
    # edgePaths = util.Queue()
    # visited = []
    # path = []
    # start = problem.getStartState()
    # currentNode = (start, [])

    # if problem.isGoalState(start):
    #     return []

    # #visited.add(start) #"mark the current node as visited and enqueue it to 'unvisisted' which actually stores nodes to visit"
    # unvisited.push((start, []))

    # while not unvisited.isEmpty():
    #     currentNode = unvisited.pop()
    #     if currentNode[0] not in visited:
    #         visited.append(currentNode[0])
    #         if problem.isGoalState(currentNode[0]):
    #             return path
    #         successors = problem.getSuccessors(currentNode[0])
    #         for successor in successors:
    #             if successor[0] not in visited:
    #                 unvisited.push((successor[0], currentNode[1] + [successor[1]]))
    #             #edgePaths.push(path + [successor[1]])

    #     # if (problem.isGoalState(currentNode[0])):
    #     #     path = currentNode[1]
    #     # else: 
    #     #     return []

    # return path



def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"

    unvisited = util.PriorityQueue()
    unvisited.push((problem.getStartState(), [], 0), 0)
    visited = []
    while not unvisited.isEmpty():
        current = unvisited.pop()
        currentState = current[0]
        if currentState not in visited:
            visited.append(currentState)
            if problem.isGoalState(currentState):
                return current[1]
            for each in problem.getSuccessors(currentState):
                if each[0] not in visited:
                    unvisited.push((each[0], current[1] + [each[1]], current[2] + each[2]), current[2] + each[2])

    # unvisited = util.PriorityQueue()
    # edgePaths = util.PriorityQueue()
    # visited = []
    # path = []
    # start = problem.getStartState()
    # currentNode = (start, [])

    # if problem.isGoalState(start):
    #     return []

    # unvisited.push((start, path), 0)

    # while not unvisited.isEmpty():
    #     if problem.isGoalState(currentNode[0]):
    #         return path

    #     if currentNode[0] not in visited:
    #         visited.append(currentNode[0])
    #         successors = problem.getSuccessors(currentNode[0])
    #         for successor in successors:
    #             cost = problem.getCostOfActions(path)
    #             unvisited.push((successor[0], currentNode[1] + [successor[1]]), cost)

    #     currentNode = unvisited.pop()

    #     if (problem.isGoalState(currentNode[0])):
    #         path = currentNode[1]

    # return path
    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"

    # unvisited = util.PriorityQueue()
    # edgePaths = util.PriorityQueue()
    # visited = []
    # path = []
    # start = problem.getStartState()
    # currentNode = (start, [])

    # if problem.isGoalState(start):
    #     return []

    # unvisited.push((start, path), 0)

    # while not unvisited.isEmpty():
    #     if problem.isGoalState(currentNode[0]):
    #         return path

    #     if currentNode[0] not in visited:
    #         visited.append(currentNode[0])
    #         successors = problem.getSuccessors(currentNode[0])
    #         for successor in successors:
    #             cost = problem.getCostOfActions(path)
    #             weight = heuristic(currentNode[0], problem) + cost
    #             unvisited.push((successor[0], currentNode[1] + [successor[1]]), weight)

    #     currentNode = unvisited.pop()

    #     if (problem.isGoalState(currentNode[0])):
    #         path = currentNode[1]

    # #return path

    unvisited = util.PriorityQueue()
    unvisited.push((problem.getStartState(), [], 0), 0)
    visited = []
    while not unvisited.isEmpty():
        current = unvisited.pop()
        currentState = current[0]
        if currentState not in visited:
            visited.append(currentState)
            if problem.isGoalState(currentState):
                return current[1]
            for each in problem.getSuccessors(currentState):
                if each[0] not in visited:
                    unvisited.push((each[0], current[1] + [each[1]], current[2] + each[2] + heuristic(each[0], problem)
                                  - heuristic(current[0], problem)), current[2] + each[2] + heuristic(each[0], problem)
                                  - heuristic(current[0], problem))
    


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
