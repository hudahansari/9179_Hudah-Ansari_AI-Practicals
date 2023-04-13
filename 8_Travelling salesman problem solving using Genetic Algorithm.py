def tsp(n, cost):
    # Initialization
    C = [0] * (n + 1)
    visits = [0] * n
    total_cost = 0
    e = 0
    
    # Start with city 1
    C[0] = 1
    visits[0] = 1
    
    # Find the shortest path to the next city
    for r in range(1, n):
        minimum = float('inf')
        for j in range(n):
            if visits[j] == 0 and cost[e][j] < minimum:
                minimum = cost[e][j]
                k = j
        visits[k] = 1
        C[r] = k+1
        total_cost += minimum
        e = k
    
    # Return the visited cities and total cost
    C[n] = 1
    total_cost += cost[e][0]
    print("Visited cities: ", C)
    print("Total cost: ", total_cost)

# Take input for the number of cities
n = int(input("Enter the number of cities: "))

# Take input for the cost matrix
cost = []
print("Enter the cost matrix:")
for i in range(n):
    row = list(map(int, input().split()))
    cost.append(row)

# Call the tsp function
tsp(n, cost)
