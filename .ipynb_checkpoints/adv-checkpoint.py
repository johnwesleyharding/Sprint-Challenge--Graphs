from room import Room
from player import Player
from world import World
from graph import Graph
from ast import literal_eval

world = World()
map_file = "maps/main_maze.txt"
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
player = Player(world.starting_room)
g = Graph()
explored = {0}
location = 0
traversal_path = []

for node in room_graph:
    
    if node not in g.vertices:
        
        g.add_vertex(node)
        
    for target in room_graph[node][1].values():
        
        g.add_edge(node, target)

while len(explored) < len(room_graph):

    route = g.quick_path(location, explored)
    step = 1
    
    while location != route[-1]:
        
        moved = False
        
        for d in room_graph[location][1]:
            
            if moved == False:
                
                move = room_graph[location][1][d]

                if move == route[step]:

                    moved = True
                    step += 1
                    traversal_path.append(d)
                    location = move
                    explored.add(move)

visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")
