class Graph:

    def __init__(self):
        
        self.vertices = {}

    def add_vertex(self, vertex_id):
        
        self.vertices[vertex_id] = set()
        
    def add_edge(self, node, target):
        
        if target not in self.vertices:
            
            self.add_vertex(target)
            
        self.vertices[node].add(target)
            
    def get_paths(self, node, explored):
        
        visited = {node: [node]}
        current = {node: self.vertices[node]}
        flag = True
        
        while flag:
            
            layer = {}
            flag = False
            
            for room in current:
                
                for path in current[room]:
                
                    if path not in visited:
                        
                        visited[path] = visited[room][:]
                        visited[path].append(path)
                        layer[path] = self.vertices[path]
                        flag = True
            
            current = layer
        
        for loc in explored:
            
            visited.pop(loc)
            
        return visited
    