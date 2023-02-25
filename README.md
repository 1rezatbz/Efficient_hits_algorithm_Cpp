# Efficient Implementation of HITS Algorithm for Large Datasets in C++


## Description

* The HITS (Hyperlink-Induced Topic Search) algorithm is a link analysis algorithm used to rate web pages. It is used to analyze web link structures to discover and rank web pages relevant to a particular search. The algorithm uses hubs and authority ranks to define a recursive relationship between web pages.

* This project contains an implementation of the HITS algorithm in C++. It provides a parallelized iterative approach to computing the hub and authority scores for a given graph.

## Implementation

* The HITS algorithm is implemented using the power iteration method, which iteratively calculates the hub and authority scores for each node in the graph. The algorithm stops iterating when either the maximum number of iterations is reached or the change in scores is below a given stop epsilon.

* The implementation uses multi-threading to improve performance. The graph is split into smaller subgraphs, and each subgraph is processed by a separate thread. The results are then combined to obtain the final scores.
## Getting Started

Here are the steps to get started with this project:

1. Clone this repository to your local machine.
2. Navigate to the root directory of the project.
3. Run `cmake .` to generate the Makefile.
4. Run `make` to compile the code.
5. Use

## Prerequisites

To use this project, you will need the following:

* C++ compiler (e.g. g++ or clang++)
* CMake
* Google Test

## Usage

the `ParallelIterativeHits` function is provided to compute the hub and authority scores for a given graph. The function takes a HitsGraph object, which represents a directed, unweighted graph. The maximum number of iterations and stop epsilon values can be adjusted to control the accuracy of the results.
```c++
#include "hits.hpp"

// create graph with 5 nodes and 6 edges
std::vector<hits_alg::EdgePair> edges{{0,1}, {1,2}, {2,3}, {3,1}, {1,4}, {4,0}};
hits_alg::HitsGraph graph(5, 6, edges);

// run HITS algorithm with max 100 iterations and stop epsilon of 10e-6
auto [hub_scores, auth_scores] = hits_alg::ParallelIterativeHits(graph, 100, 10e-6);
```

## Google Test
Google Test is a popular C++ unit testing framework developed by Google. It allows developers to write tests for their code, ensuring that it works as expected and is free of bugs. To use Google Test, you need to install it first.

To install Google Test, you can download the source code from the official GitHub repository and build it yourself, or you can use a package manager if it's available on your system. For example, if you're using Ubuntu, you can install Google Test using the following command:

> sudo apt-get install libgtest-dev

Once you have installed Google Test, you can create test cases for your code using the framework's API. Google Test provides a rich set of macros and assertions that make it easy to write tests and check the results. You can run the tests using a test runner, which will execute the test cases and report the results.
## Contributing

Contributions and ideas are welcome! If you would like to contribute, please submit a pull request or contact me directly.


<!-- CONTACT -->
### Contact

Reza Tabriz - [@linkedin](https://www.linkedin.com/in/rezatbz/) - 1rezartabriz@gmail.com

