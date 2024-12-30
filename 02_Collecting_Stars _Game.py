n = int(input())  # Size of the square field

# Read the matrix and initialize player position and stars
matrix = []
player_position = []
stars_collected = 2

for row in range(n):
    line = input().split()
    matrix.append(line)
    if "P" in line:
        player_position = [row, line.index("P")]
        matrix[row][player_position[1]] = "."  # Mark starting position as visited

# Define movement directions
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

# Process commands until the player collects 10 stars or runs out of stars
while 0 < stars_collected < 10:
    command = input()

    # Calculate new position
    next_row = player_position[0] + directions[command][0]
    next_col = player_position[1] + directions[command][1]

    # Check for boundaries
    if not (0 <= next_row < n and 0 <= next_col < n):
        # Teleport to starting position if out of bounds
        next_row, next_col = 0, 0

    # Process the cell
    if matrix[next_row][next_col] == "*":
        stars_collected += 1
        matrix[next_row][next_col] = "."  # Mark star as collected
    elif matrix[next_row][next_col] == "#":
        stars_collected -= 1
        continue  # Skip updating the player position

    # Update player position
    player_position = [next_row, next_col]

# Determine the game result
if stars_collected == 10:
    print("You won! You have collected 10 stars.")
else:
    print("Game over! You are out of any stars.")

# Output the final position
print(f"Your final position is [{player_position[0]}, {player_position[1]}]")

# Mark player's final position on the matrix
matrix[player_position[0]][player_position[1]] = "P"

# Print the final state of the matrix
for row in matrix:
    print(" ".join(row))
