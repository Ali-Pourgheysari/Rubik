import json
import copy
from queue import PriorityQueue

class RubickState:

    def __init__(self, state):
        self.state = state
        self.neighbors = self.get_neighbors()


    def rotate_clockwise(self, color):
        temp_state = copy.deepcopy(self.state)
        if color == 'w':
            for item in self.state:
                if item == color:
                    for i in range(3):
                        for j in range(3):
                            temp_state[color][i][j] = self.state[color][2-j][i]
                if item == 'r':
                    for i in range(3):
                        temp_state['r'][0][i] = self.state['b'][0][i]
                if item == 'b':
                    for i in range(3):
                        temp_state['b'][0][i] = self.state['o'][0][i]
                if item == 'o':
                    for i in range(3):
                        temp_state['o'][0][i] = self.state['g'][0][i]
                if item == 'g':
                    for i in range(3):
                        temp_state['g'][0][i] = self.state['r'][0][i]
        if color == 'r':
            for item in self.state:
                if item == color:
                    for i in range(3):
                        for j in range(3):
                            temp_state[color][i][j] = self.state[color][2-j][i]
                if item == 'w':
                    for i in range(3):
                        temp_state['w'][0][i] = self.state['g'][i][2]
                if item == 'g':
                    for i in range(3):
                        temp_state['g'][i][2] = self.state['y'][0][i]
                if item == 'y':
                    for i in range(3):
                        temp_state['y'][0][i] = self.state['b'][2-i][0]
                if item == 'b':
                    for i in range(3):
                        temp_state['b'][2-i][0] = self.state['w'][0][i]
        if color == 'g':
            for item in self.state:
                if item == color:
                    for i in range(3):
                        for j in range(3):
                            temp_state[color][i][j] = self.state[color][2-j][i]
                if item == 'w':
                    for i in range(3):
                        temp_state['w'][i][2] = self.state['o'][i][2]
                if item == 'o':
                    for i in range(3):
                        temp_state['o'][i][2] = self.state['y'][2-i][0]
                if item == 'y':
                    for i in range(3):
                        temp_state['y'][i][0] = self.state['r'][i][0]
                if item == 'r':
                    for i in range(3):
                        temp_state['r'][i][0] = self.state['w'][2-i][2]
        if color == 'o':
            for item in self.state:
                if item == color:
                    for i in range(3):
                        for j in range(3):
                            temp_state[color][i][j] = self.state[color][2-j][i]
                if item == 'w':
                    for i in range(3):
                        temp_state['w'][2][i] = self.state['b'][2-i][2]
                if item == 'b':
                    for i in range(3):
                        temp_state['b'][2-i][2] = self.state['y'][2][i]
                if item == 'y':
                    for i in range(3):
                        temp_state['y'][2][i] = self.state['g'][i][0]
                if item == 'g':
                    for i in range(3):
                        temp_state['g'][i][0] = self.state['w'][2][i]
        if color == 'y':
            for item in self.state:
                if item == color:
                    for i in range(3):
                        for j in range(3):
                            temp_state[color][i][j] = self.state[color][2-j][i]
                if item == 'r':
                    for i in range(3):
                        temp_state['r'][2][i] = self.state['g'][2][i]
                if item == 'g':
                    for i in range(3):
                        temp_state['g'][2][i] = self.state['o'][2][i]
                if item == 'o':
                    for i in range(3):
                        temp_state['o'][2][i] = self.state['b'][2][i]
                if item == 'b':
                    for i in range(3):
                        temp_state['b'][2][i] = self.state['r'][2][i]
        if color == 'b':
            for item in self.state:
                if item == color:
                    for i in range(3):
                        for j in range(3):
                            temp_state[color][i][j] = self.state[color][2-j][i]
                if item == 'w':
                    for i in range(3):
                        temp_state['w'][i][0] = self.state['r'][2-i][2]
                if item == 'r':
                    for i in range(3):
                        temp_state['r'][i][2] = self.state['y'][i][2]
                if item == 'y':
                    for i in range(3):
                        temp_state['y'][i][2] = self.state['o'][2-i][0]
                if item == 'o':
                    for i in range(3):
                        temp_state['o'][i][0] = self.state['w'][i][0]
        return temp_state
        
        

    # rotate the cube counter-clockwise
    def rotate_counter_clockwise(self, color):
        temp_state = copy.deepcopy(self.state)
        if color == 'w':
            for item in self.state:
                if item == color:
                    for i in range(3):
                        for j in range(3):
                            temp_state[color][i][j] = self.state[color][j][2-i]
                if item == 'r':
                    for i in range(3):
                        temp_state['r'][0][i] = self.state['g'][0][i]
                if item == 'b':
                    for i in range(3):
                        temp_state['b'][0][i] = self.state['r'][0][i]
                if item == 'o':
                    for i in range(3):
                        temp_state['o'][0][i] = self.state['b'][0][i]
                if item == 'g':
                    for i in range(3):
                        temp_state['g'][0][i] = self.state['o'][0][i]
        if color == 'r':
            for item in self.state:
                if item == color:
                    for i in range(3):
                        for j in range(3):
                            temp_state[color][i][j] = self.state[color][j][2-i]
                if item == 'w':
                    for i in range(3):
                        temp_state['w'][0][2-i] = self.state['b'][i][0]
                if item == 'g':
                    for i in range(3):
                        temp_state['g'][i][2] = self.state['w'][0][i]
                if item == 'y':
                    for i in range(3):
                        temp_state['y'][0][2-i] = self.state['g'][2-i][2]
                if item == 'b':
                    for i in range(3):
                        temp_state['b'][2-i][0] = self.state['y'][0][i]
        if color == 'g':
            for item in self.state:
                if item == color:
                    for i in range(3):
                        for j in range(3):
                            temp_state[color][i][j] = self.state[color][j][2-i]
                if item == 'w':
                    for i in range(3):
                        temp_state['w'][2-i][2] = self.state['r'][i][0]
                if item == 'o':
                    for i in range(3):
                        temp_state['o'][i][2] = self.state['w'][i][2]
                if item == 'y':
                    for i in range(3):
                        temp_state['y'][2-i][0] = self.state['o'][i][2]
                if item == 'r':
                    for i in range(3):
                        temp_state['r'][i][0] = self.state['y'][i][0]
        if color == 'o':
            for item in self.state:
                if item == color:
                    for i in range(3):
                        for j in range(3):
                            temp_state[color][i][j] = self.state[color][j][2-i]
                if item == 'w':
                    for i in range(3):
                        temp_state['w'][2][i] = self.state['g'][i][0]
                if item == 'b':
                    for i in range(3):
                        temp_state['b'][i][2] = self.state['w'][2][2-i]
                if item == 'y':
                    for i in range(3):
                        temp_state['y'][2][i] = self.state['b'][2-i][2]
                if item == 'g':
                    for i in range(3):
                        temp_state['g'][i][0] = self.state['y'][2][i]
        if color == 'y':
            for item in self.state:
                if item == color:
                    for i in range(3):
                        for j in range(3):
                            temp_state[color][i][j] = self.state[color][j][2-i]
                if item == 'r':
                    for i in range(3):
                        temp_state['r'][2][i] = self.state['b'][2][i]
                if item == 'g':
                    for i in range(3):
                        temp_state['g'][2][i] = self.state['r'][2][i]
                if item == 'o':
                    for i in range(3):
                        temp_state['o'][2][i] = self.state['g'][2][i]
                if item == 'b':
                    for i in range(3):
                        temp_state['b'][2][i] = self.state['o'][2][i]
        if color == 'b':
            for item in self.state:
                if item == color:
                    for i in range(3):
                        for j in range(3):
                            temp_state[color][i][j] = self.state[color][j][2-i]
                if item == 'w':
                    for i in range(3):
                        temp_state['w'][i][0] = self.state['o'][i][0]
                if item == 'r':
                    for i in range(3):
                        temp_state['r'][i][2] = self.state['w'][2-i][0]
                if item == 'y':
                    for i in range(3):
                        temp_state['y'][i][2] = self.state['r'][i][2]
                if item == 'o':
                    for i in range(3):
                        temp_state['o'][i][0] = self.state['y'][2-i][2]
        return temp_state


    def get_neighbors(self):
        neighbors = []
        for color in self.state:
            neighbors.append(self.rotate_clockwise(color))
            neighbors.append(self.rotate_counter_clockwise(color))
        return neighbors
    
    def __lt__(self, other):
        return False

# A* algorithm to find the fastest way to solve the cube
def A_star(initial_state, final_state):
    # Create a priority queue
    priority_queue = PriorityQueue()

    # Add the initial state to the priority queue
    priority_queue.put((0, initial_state))

    # Create a set to store the visited states
    visited = set()

    # Create a dictionary to store the parent of each state
    parent = {}

    # Create a dictionary to store the cost of each state
    cost = {}

    # Add the initial state to the visited set
    visited.add(initial_state)

    # Add the initial state to the cost dictionary
    cost[initial_state] = 0

    # Loop until the priority queue is empty
    while not priority_queue.empty():
        # Get the state with the lowest cost
        current_state = priority_queue.get()[1]

        # If the current state is the final state, return the path
        if current_state.state == final_state.state:
            return get_path(parent, initial_state, final_state)

        # Get the neighbors of the current state
        neighbors = current_state.get_neighbors()

        # Loop through each neighbor
        for neighbor in neighbors:
            neighbor = RubickState(neighbor)
            # If the neighbor has not been visited
            if neighbor not in visited:
                # Add the neighbor to the visited set
                visited.add(neighbor)

                # Add the neighbor to the parent dictionary
                parent[neighbor] = current_state

                # Add the neighbor to the cost dictionary
                cost[neighbor] = cost[current_state] + 1

                # Add the neighbor to the priority queue
                priority_queue.put((cost[neighbor] + heuristic(neighbor, final_state), neighbor))
                n = 4

    # Return None if no path is found
    return None



# generate a heuristic function using manhattan distance
def heuristic(current_state, final_state):
    Manhattan = Manhattan_distance(current_state, final_state)
    number_of_colors = color_next_to_each_other(current_state)
    manhattan_per_number_of_colors = Manhattan/number_of_colors

    return manhattan_per_number_of_colors

# a function to calculate the number of colors next to each other
def color_next_to_each_other(current_state):
    sum = 0
    for face in current_state.state:
        for row in range(3):
            for i in range(2):
                if current_state.state[face][row][i][0] == current_state.state[face][row][i+1][0]:
                    sum += 1
        for col in range(3):
            for i in range(2):
                if current_state.state[face][i][col][0] == current_state.state[face][i+1][col][0]:
                    sum += 1
    return sum

# Manhattan distance
def Manhattan_distance(current_state, final_state):
    # Create a dictionary to store the coordinates of each color
    sum = 0
    color_dic = {'w': 'y', 'r': 'o', 'g': 'b', 'y': 'w', 'o': 'r', 'b': 'g'}
    for i, face in enumerate(current_state.state):
        for j, row in enumerate(current_state.state[face]):
            for k, color in enumerate(row):
                for i2, face2 in enumerate(final_state.state):
                    for j2, row2 in enumerate(final_state.state[face2]):
                        for k2, color2 in enumerate(row2):
                            z = 0
                            if color == color2:
                                if face == face2: 
                                    z = 0
                                elif face == color_dic[face2]:
                                    z = 2
                                else:
                                    z = 1
                                
                                sum += abs(j - j2) + abs(k - k2) + z
                                
    # Return the manhattan distance
    return sum

def get_path(parent, initial_state, final_state):
    # Create a list to store the path
    path = []

    # Add the final state to the path
    path.append(final_state)

    # Loop until the parent dictionary is empty
    while final_state != initial_state:
        for item in parent:
            if item.state == final_state.state:
                final_state = item
                break
        # Get the parent of the current state
        current_state = parent.pop(final_state)

        # Add the parent to the path
        path.append(current_state)

        # Set the current state to the parent
        final_state = current_state

    # Return the path
    return path

def get_input(JSON_name):
    initial_list = []
    final_list = []

    with open(JSON_name) as f:
        data = json.load(f)

    for color in ['w', 'r', 'g', 'o', 'y', 'b']:
        initial_list.append(data['start'][color])
        final_list.append(data['end'][color])

    return initial_list, final_list

def turn_to_dic(input_list):
    output_dic = {}
    for item in input_list:
        output_dic[item[1][1][:1]] = item
    return output_dic

if __name__ == "__main__":
    initial_list = []
    final_list = []

    JSON_name = input("Enter the name of the JSON file: ")
    output_file_name = 'output.json'

    initial_list, final_list = get_input(JSON_name)
    initial_state = RubickState(turn_to_dic(initial_list))
    final_state = RubickState(turn_to_dic(final_list))
    path = A_star(initial_state, final_state)
