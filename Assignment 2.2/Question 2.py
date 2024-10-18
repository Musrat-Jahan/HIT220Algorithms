from collections import deque, defaultdict

def findMHTs(n, edges):
    if n == 1:
        return [0]
    
    # Build the graph as an adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    def bfs(start):
        dist = [-1] * n
        q = deque([start])
        dist[start] = 0
        farthest_node = start
        
        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                if dist[neighbor] == -1:
                    dist[neighbor] = dist[node] + 1
                    q.append(neighbor)
                    if dist[neighbor] > dist[farthest_node]:
                        farthest_node = neighbor
        return farthest_node, dist
    
    # Find the farthest node from an arbitrary node (node 0)
    farthest_node_1, _ = bfs(0)
    
    # Find the farthest node from farthest_node_1 to determine the diameter
    farthest_node_2, dist_from_1 = bfs(farthest_node_1)
    
    # Find the distance from farthest_node_2
    _, dist_from_2 = bfs(farthest_node_2)
    
    # The diameter is the distance between farthest_node_1 and farthest_node_2
    diameter = dist_from_1[farthest_node_2]
    
    # Find the centers of the tree
    centers = []
    for i in range(n):
        if dist_from_1[i] == diameter // 2 or dist_from_2[i] == diameter // 2 or \
           dist_from_1[i] == (diameter + 1) // 2 or dist_from_2[i] == (diameter + 1) // 2:
            if dist_from_1[i] + dist_from_2[i] == diameter:
                centers.append(i)
    
    return centers

# Read user input
def main():
    n = int(input("Enter the number of nodes: "))
    edges = []
    print(f"Enter {n - 1} edges in the format 'a b' (one edge per line):")
    for _ in range(n - 1):
        a, b = map(int, input().split())
        edges.append([a, b])
    
    # Find Minimum Height Trees
    mhts = findMHTs(n, edges)
    
    if mhts:
        print("Minimum Height Trees roots:", mhts)
    else:
        print("The provided graph is not a valid tree.")

# Example usage:
main()