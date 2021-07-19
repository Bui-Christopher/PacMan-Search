# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
from typing import Any

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # open := [start]
    startNode = problem.getStartState()
    # fringe uses stack (LIFO)
    fringe = util.Stack()
    # create an empty list for actions we need to take
    actions = []
    # create an empty list for cost
    cost = []
    # begin
    fringe.push((startNode, actions, cost))
    # closed := []
    closed = []
    # while not open [] do
    while True:
        if fringe.isEmpty():
            break
        # remove leftmost state from open, call it x
        currentNode, actions, cost = fringe.pop()
        # if x is a goal then return success
        if problem.isGoalState(currentNode):
            return actions
        # put x on closed
        if not currentNode in closed:
            closed.append(currentNode)
        # generate children of x
        for successor, action, stepCost in problem.getSuccessors(currentNode):
            # discard children of x if already on open or closed
            if not successor in closed:
                # put remaining children on left end of open
                finalAction = actions + [action]
                finalCost = cost + [stepCost]
                fringe.push((successor, finalAction, finalCost))
    return []
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #use queue to perform the BFS Algorithm
    open = util.Queue()
    startState = problem.getStartState()
    closed = []
    
    #add the start state of the problem to the queue
    open.push((startState, []))
    
    #loop thru until the open queue is empty
    while not open.isEmpty():
    
        #remove leftmost state from open and call it current
        current, actions = open.pop()
        
        #push the current stage if it is not in closed
        if not current in closed:
            #push to visted
            closed.append(current)
            
            #if goalstate return actions
            if problem.isGoalState(current):
                return actions
            else:
                #generate childrent of current
                for childState, childAction, childCost in problem.getSuccessors(current):
                
                    #discard children if areadly open or closed
                    open.push((childState, (actions + [childAction])))
    return actions

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    open = util.PriorityQueue()
    startState = problem.getStartState()
    closed = []
    
    #get state, action, cost
    open.push((startState, [], 0), 0)
    
    #loop that through the states until open is empty
    while not open.isEmpty():
    
        #explore first state
        current, actions, cost = open.pop()
        
        if not current in closed:
           
            #add to closed if not in closed
            closed.append(current)
            
            #check if current state is the goal state
            if problem.isGoalState(current):
                return actions
                
            #loop through the successors
            for state, newAction, newCost in problem.getSuccessors(current):
                if not state in closed:
                
                    #calculate the heuristic value
                    heuristicValue = cost + newCost + heuristic(state, problem)
                    newState = (state, actions + [newAction], cost + newCost)
                    open.push(newState, heuristicValue)
    
    return actions


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
