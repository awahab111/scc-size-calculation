# Strongly Connected Component (SCC) Size Calculation
This project focuses on computing the size of the Strongly Connected Component (SCC) in a given directed graph. A strongly connected component is a partition of a directed graph in which there is a path from each vertex to another vertex in the partition. The project utilizes the Depth First Search (DFS) algorithm to compute the SCC.

## Introduction
The goal of this project is to calculate the size of the largest SCC in a directed graph. The project uses two main functions, implemented by the author, which are:

**create_adjacency_list(filename)**: This function reads the graph data from a file and creates an adjacency list representation of the directed graph.
**scc_iterative_dfs(vertices, edges)**: This function performs an iterative DFS to compute the SCCs in the graph and returns them one by one.
### Dataset
To perform the SCC size calculation, the project uses two datasets:

**Google Web Graph**: This dataset represents the web graph of Google, containing web pages as nodes and hyperlinks as directed edges.

**Twitter Web Graph**: This dataset represents the social network graph of Twitter, with users as nodes and follows relationships as directed edges.
You can download the datasets from the provided links and use them as input for the project.

## Usage
To use this project, you can follow these steps:

1. Clone the repository: 
``` bash 
git clone https://github.com/awahab111/scc-size-calculation.git
```
2. Navigate to the project directory:
``` bash
cd scc-project
```
3. Place the dataset files in the project directory.
4. Run the main.py script:
``` 
python main.py
```
5. The script will process the graphs and output the size of the largest SCC for each dataset.

## Example Output
Here's an example of the expected output from running the main.py script:
```
Enter the name of the input file: web-Google.txt
Processing web-Google.txt ...
Nodes in largest SCC:
434818
```
## Additional Resources
In addition to the custom functions implemented in the project, the following resources have been incorporated:

**graph.py**: Contains the implementation of create_adjacency_list and get_vertices functions for creating the graph representation and retrieving the vertices.
**scc.py**: Contains the implementation of scc_iterative_dfs and largest_scc functions for performing the SCC calculation.

## Contribution

Contributions to this project are welcome. You can contribute by opening issues for bug reports or feature requests, and by submitting pull requests with improvements to the code.

Please ensure that your contributions align with the goals of the project and follow the guidelines provided in the repository.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for personal or commercial purposes. See the `LICENSE` file for more details.
