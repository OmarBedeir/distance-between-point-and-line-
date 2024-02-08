import math
import matplotlib.pyplot as plt

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_shortest_distance(x1, y1, x2, y2, x3, y3, x4, y4):
    # Calculate the distance between the first and second points
    distance = calculate_distance(x1, y1, x2, y2)

    # Calculate the coordinates of the point (x4, y4) on the line between the first and second points
    x4_on_line = ((x2 - x1) * (y4 - y1)) / (y2 - y1) + x1
    y4_on_line = ((y2 - y1) * (x4_on_line - x1)) / (x2 - x1) + y1

    # Calculate the distance between (x4, y4) and the first and second points
    shortest_distance = calculate_distance(x4, y4, x4_on_line, y4_on_line)

    # Plot the points and lines
    plt.scatter([x1, x2, x3, x4], [y1, y2, y3, y4], color='blue', label='Points')
    plt.plot([x1, x2], [y1, y2], color='black', label='Line between Point 1 and 2')
    plt.scatter(x4_on_line, y4_on_line, color='red', label='Point (x4, y4) on Line')

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.show()

    return shortest_distance

# Define the points
x1, y1 = 1, 2
x2, y2 = 4, 6
x3, y3 = 7, 8
x4, y4 = 5, 4

# Calculate the shortest distance between the fourth point and the line between the first and second points
shortest_distance = calculate_shortest_distance(x1, y1, x2, y2, x3, y3, x4, y4)
print(f"Shortest distance between the fourth point and the line: {shortest_distance}")
