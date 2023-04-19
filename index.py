
import copy


class RubickState:

    def __init__(self, state):
        self.state = state


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
        
        

    