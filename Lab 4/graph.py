from collections import defaultdict
import random

graph = defaultdict(list)

def addEdge(graph,u,v):
	graph[u].append(v)


city_list = ["Bombay", "Singapore", "Kuala Lumpur", "Jakarta", "Bangkok", "Beijing", "Shanghai", "Seoul", "Hong Kong", "Tokyo", "Sydney", "Perth", "New Zealand", "Washington D.C.", "New York", "Los Angeles","Chicago", "Seattle", "Boston", "London", "Amsterdam", "Berlin", "Copenhagen", "Moscow", "Paris","Rome", "Toronto", "Cairo", "Istanbul", "Dubai", "Madrid", "Las Vegas", "Prague", "Budapest", "Munich", "Zurich", "Vancouver", "Melbourne", "Rio De Janeiro", "Frankfurt"]
print(len(city_list))
n = int(input("Enter number of cities(max 40): "))

print("\nList of Cities:")
for i in range(n):
    print(i+1 , city_list[i])

#PROBLEM: loop condition must be until number of keys is not equal to number of cities wanted
def CreateGraph(graph):
    x = 0
    while x<=n:
        city_list1 = city_list[:n]
        u = random.choice(city_list1)
        v = random.choice(city_list1)
        while(v==u):
            v = random.choice(city_list1)
        if v not in graph[u]:
            addEdge(graph, u, v)

        if u not in graph[v]:
            addEdge(graph, v, u)

        x+=1

CreateGraph(graph)
#NEED A PRINT GRAPH FUNCTION
print(graph)
print(len(graph))

# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    explored = []           # keep track of explored nodes
    queue = [[start]]       # keep track of all the paths to be checked

    if start == goal:
        return "That was easy! Start = goal"

    while queue:                # keeps looping until all possible paths have been checked
        path = queue.pop(0)     # pop the first path from the queue
        node = path[-1]         # get the last node from the path
        if node not in explored:
            neighbours = graph[node]    # go through all neighbour nodes, construct a new path and push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:           # return path if neighbour is goal
                    return new_path

            #mark node as explored
            explored.append(node)

    #in case there's no path between the 2 nodes
    return "Sorry, but a connecting path doesn't exist :("

source = input("\nWhich city do you want to select as source?")
destination = input("\nWhich city do you want to select as destination?")
print("Shortest path: ", bfs_shortest_path(graph, source, destination))

#GET CPU TIMES FOR DIFFERENT SIZES OF GRAPHS
