def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def dfs_paths(graph, start, end):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == end:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def main():
    graph = {'A': {'B', 'C'},
             'B': {'A', 'D', 'E'},
             'C': {'A', 'F', 'G'},
             'D': {'B'},
             'E': {'B', 'H'},
             'F': {'C'},
             'G': {'C'},
             'H': {'E'},
    }

    print(list(dfs_paths(graph, 'H', 'F')))
    print(list(dfs(graph, 'H')))

if __name__ == "__main__":
    main()