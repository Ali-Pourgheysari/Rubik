# Rubik's Cube Solver
 This Python script implements an A* algorithm to find the fastest way to solve a Rubik's Cube. The code allows the user to input the initial and final states of the Rubik's Cube in a JSON file and outputs the steps needed to solve it in another JSON file.

 ## How to use
 1. Prepare a JSON file (e.g., rubik_input.json) containing the initial and final states of the Rubik's Cube. The states should be represented as a dictionary, where the keys are the face colors (w, r, g, o, y, b) and the values are 2D arrays representing the colors of the 3x3 cube faces. [THIS](sample.json) is an example of a valid input file and [THIS](sample.png) is the corresponding Rubik's Cube.

2. Run the script, and it will prompt you to enter the name of the JSON file containing the input. For example, enter `rubik_input.json`.

3. The script will output the steps needed to solve the Rubik's Cube in a new JSON file named `output.json`. The output file will contain a dictionary with the key `"steps"` indicating the number of steps needed to solve the cube. Additionally, the cube states for each step will be written to the file.

4. The heuristic function used to guide the A* search is based on the Manhattan distance between the current state and the final state of the Rubik's Cube. The number of colors next to each other is also considered in the heuristic calculation. The better heuristic would be the sum of number of moves needed to move each color to its correct position, but this would require a lot of computation. 

Feel free to explore and optimize the Rubik's Cube solver with different initial states and experiment with alternative heuristic functions to improve its efficiency and performance. Happy cubing! 🧊