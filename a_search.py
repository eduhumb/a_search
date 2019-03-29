# A* search is both complete and optimal
# f(n) = g(n) + h(n) - is the estimated cost of the cheapest solution through 'n'
# g(n) - is the cost to reach the node 'n'
# h(n) - is the the cost to get from the node 'n' to the goal 

import json

class Main:
    def __init__(self):
        with open('graph_2.json') as f:
            self.graph = json.load(f)
            self.previous = None

    def get_lowest_f_score(self, open_set):
        f_score = {}
        if not self.previous:
            return open_set[0]
        else:
            for city in open_set:
                f = self.graph['g'][current][city] + self.graph['h'][city]
                f_score[city] = f

            return min(f_score, key=f_score.get)

    def generate_successors(self, current):
        return self.graph['g'][current]

    def reconstruct_path(self,came_from, current):
        total_path = [current]
        while current in came_from.keys():
            current = came_from[current]
            total_path.append(current)
        return total_path

    def a_star(self, start, goal):

        # The set of nodes already evaluated
        closed_set = []

        # The set of currently discovered nodes that are not evaluated yet.
        # Initially, only the start node is known.
        open_set = [start]

        #  For each node, which node it can most efficiently be reached from.
        #  If a node can be reached from many nodes, cameFrom will eventually contain the
        #  most efficient previous step.
        came_from = {}

        # For each node, the cost of getting from the start node to that node.
        g_score = {}

        # The cost of going from start to start is zero.
        g_score[start] = 0

        # For each node, the total cost of getting from the start node to the goal
        # by passing by that node. That value is partly known, partly heuristic.
        f_score = {}

        # For the first node, that value is completely heuristic.
        f_score[start] = self.graph['h'][start]

        while open_set:

            current = self.get_lowest_f_score(open_set)

            if current == goal:
                print(self.reconstruct_path(came_from, current))

            open_set.remove(current)
            closed_set.append(current)

            successors = self.generate_successors(current)

            for neighbor in successors.items():

                # Ignore the neighbor which is already evaluated.
                if neighbor[0] in closed_set:                                             
                    continue		            

                # The distance from start to a neighbor
                tentative_g_score = g_score[current] + neighbor[1][0]

                # Discover a new node
                if neighbor[0] not in open_set:	 
                    open_set.append(neighbor[0])
                elif tentative_g_score >= g_score[neighbor[0]]:
                    continue

                # This path is the best until now. Record it!
                came_from[neighbor[0]] = current
                g_score[neighbor[0]] = tentative_g_score
                f_score[neighbor[0]] = g_score[neighbor[0]] + neighbor[1][1]

g = Main()
g.a_star("Arad", "Bucharest")