def find_shortest_path(grid, start_node, end_node):

    if not grid: return []
    
    def neighbors(node):
        x = node.position.x
        y = node.position.y
        return [grid[a][b] for a, b in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
                if 0 <= a and a < len(grid) and 0 <= b and b < len(grid[a]) and grid[a][b].passable]

    distance = {}
    node = start_node
    dst = 0
    distance[node] = dst
    visited_a, visited_b = set(), set()

    while not node is end_node:
        for n in neighbors(node):
            if not n in distance:
                distance[n] = dst + 1
                visited_b.add(n)
        if not visited_a:
            visited_a, visited_b = visited_b, set()
            dst += 1
        node = visited_a.pop()

    path = [node]

    while dst > 0:
        dst -= 1
        node = next(n for n in neighbors(node) if distance[n] == dst)
        path.append(node)

    assert node is start_node
    path.reverse()
    return path
