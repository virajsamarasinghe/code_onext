#python3

MOD = 10**9 + 7

def count_valid_messages(N, constraints):
    def backtrack(pos, current_string):
        """ Backtracking to generate all valid binary strings """
        nonlocal valid_count

        # If we reach the end of the string
        if pos == N:
            # Check constraints only on complete strings
            for i, j in constraints:
                if current_string[i - 1] == current_string[j - 1]:  # i and j are 1-indexed
                    return  # Invalid string, stop further processing
            valid_count += 1  # Valid string found
            return

        # Add '0' at current position and recurse
        backtrack(pos + 1, current_string + '0')

        # Add '1' at current position and recurse
        backtrack(pos + 1, current_string + '1')

    valid_count = 0
    backtrack(0, "")
    return valid_count % MOD

# Input handling
if __name__ == "__main__":
    N = int(input())  # Length of the quantum message
    K = int(input())  # Number of constraints
    constraints = [tuple(map(int, input().split())) for _ in range(K)]
    print(count_valid_messages(N, constraints))




