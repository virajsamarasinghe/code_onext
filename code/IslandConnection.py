import math
import heapq

def minimum_cost_to_connect_islands(n, islands):
    # Helper function to calculate the bridge cost
    def bridge_cost(island1, island2):
        x1, y1, c1 = island1
        x2, y2, c2 = island2
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance * (c1 + c2)

    # Prim's Algorithm for Minimum Spanning Tree
    visited = [False] * n
    min_heap = [(0, 0)]  # (cost, island_index)
    total_cost = 0
    edges_used = 0

    while edges_used < n:
        cost, current_island = heapq.heappop(min_heap)

        if visited[current_island]:
            continue

        # Mark the island as visited and add the cost
        visited[current_island] = True
        total_cost += cost
        edges_used += 1

        # Add all neighboring islands to the heap
        for next_island in range(n):
            if not visited[next_island]:
                bridge_cost_to_next = bridge_cost(islands[current_island], islands[next_island])
                heapq.heappush(min_heap, (bridge_cost_to_next, next_island))

    return round(total_cost, 2)

# Read input
if __name__ == "__main__":
    # Parse the input
    n = int(input())
    islands = eval(input())
    
    # Compute the result
    result = minimum_cost_to_connect_islands(n, islands)
    print(f"{result:.2f}")
