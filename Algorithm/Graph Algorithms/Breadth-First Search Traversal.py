import collections
def bfs(graph,root):
    visited = set()
    queue = collections.deque([root])
    visited.add(root)

    while queue:
        vertex = queue.popleft()
        print(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {0:[1,2],1:[0,3,4],2:[0,5],3:[1,4],4:[1,3],5:[1,2]}
bfs(graph,2)