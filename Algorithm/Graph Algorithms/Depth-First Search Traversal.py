def dfs(graph,root):
    visited = set()
    stack = [root]
    
    while stack:
        vertex = stack.pop()
        if(vertex not in visited):
            print(vertex)
            visited.add(vertex)
            stack.extend(graph[vertex])

graph = {0:[1,2],1:[0,3,4],2:[0,5],3:[1,4],4:[1,3],5:[1,2]}
dfs(graph,2)