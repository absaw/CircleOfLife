# CircleOfLife

AI Project - Circle of Life - Probablistic Modeling with Graphs

Flow of Project -- 
Starting Point = Main.py -- Used to call agents according to user's input

Agent Files --
Each agent has its own class file. This agent class is simulated using the agent's simulator file.
Simulator file executes 30 trials. Each trial runs the agent on 100 randomized mazes. The metrics are calculated 
independently for each trial. The average of all trials is taken to generate the summary.

Results --
Each agent has a text and csv file. Text file has the simulation wise results and the summary. Csv file has the 
simulation wise detailed results.