
# //Python3


def max_water_retention(n, heights):
    # Function to calculate water retention with the current heights
    def calculate_water(heights):
        left_max = [0] * n
        right_max = [0] * n
        water = 0
        
        # Compute the left_max array
        left_max[0] = heights[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], heights[i])
        
        # Compute the right_max array
        right_max[n - 1] = heights[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], heights[i])
        
        # Calculate the total water trapped
        for i in range(n):
            water += max(0, min(left_max[i], right_max[i]) - heights[i])
        
        return water
    
    # Step 1: Calculate the initial water retention without any repairs
    initial_water = calculate_water(heights)
    max_water = initial_water
    
    # Step 2: Try repairing each wall individually
    for i in range(n):
        # Increase the height of the i-th wall by 1
        heights[i] += 1
        # Calculate the new water retention after the repair
        new_water = calculate_water(heights)
        max_water = max(max_water, new_water)
        # Restore the original height of the i-th wall
        heights[i] -= 1
    
    # Step 3: Try repairing a second wall and calculate the best possible water retention
    for i in range(n):
        for j in range(i + 1, n):
            # Increase the height of the i-th and j-th walls by 1
            heights[i] += 1
            heights[j] += 1
            # Calculate the new water retention after both repairs
            new_water = calculate_water(heights)
            max_water = max(max_water, new_water)
            # Restore the original heights of the i-th and j-th walls
            heights[i] -= 1
            heights[j] -= 1
    
    return max_water


# Reading the input
n = int(input())  # number of walls
heights = list(map(int, input().split()))  # heights of the walls

# Output the result
print(2*max_water_retention(n, heights))
