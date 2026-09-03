import heapq

graph = {
    'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Pitesti', 138)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Pitesti', 97)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': []
}

heuristic = {
    'Arad': 366,
    'Zerind': 374,
    'Oradea': 380,
    'Timisoara': 329,
    'Lugoj': 244,
    'Mehadia': 241,
    'Drobeta': 242,
    'Craiova': 160,
    'Sibiu': 253,
    'Fagaras': 176,
    'Rimnicu Vilcea': 193,
    'Pitesti': 100,
    'Bucharest': 0
}

def astar(start, goal):
    queue = []
    heapq.heappush(queue, (heuristic[start], 0, start, [start]))
    visited = []

    while queue:
        f, g, city, path = heapq.heappop(queue)

        print(city, "g =", g, "h =", heuristic[city], "f =", f)

        if city == goal:
            return path, g

        if city in visited:
            continue

        visited.append(city)

        for neighbor, distance in graph[city]:
            if neighbor not in visited:
                new_g = g + distance
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(queue, (new_f, new_g, neighbor, path + [neighbor]))


path, cost = astar("Arad", "Bucharest")

print("\nShortest Path:")
for city in path:
    print(city)

print("\nTotal Cost:", cost)
