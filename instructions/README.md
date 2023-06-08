# Summative Research Project

For this assignment, you will be researching an algorithm or data structure not covered in the course.
You will be writing a report on the algorithm or data structure, and
you will be implementing it in **a programming language of your choice**. You will be presenting your
research and implementation as part of the repository submission.

## Deliverables:

- The report should be written in markdown, and as your [README.md](../README.md) file for the repository.
- All code written should be provided
- Tests for code should be provided
- Any related files and evidence of running the algorithm/datastructure should be provided.

From your deliverables, we should not only be able to see a valid implementation, but that you confirmed and fully
tested it in addition to the report.

## Details:

This is an open ended research project with the condition it must be an algorithm or data structure not covered in the course.
With that said, it can be difficult to select a topic. Here are some suggestions:

- B+ Trees
- AVL Tree
- Heap Data Structure (if you do this, make sure you include comparison of implementations)
- Cartesian Tree
- R+ Tree
- Red–black tree
- Sorted Hashmap
- (Really, you can look at the java collections interface and get a bunch of ideas of what to implement)

For some algorithms, you may want to consider implementing a specific algorithm, or a specific type of algorithm.

- KnapSack
- K-Nearest Neighbors
- Lagged Fibonacci generator (or other Pseudorandom number generator)
- Ford–Fulkerson algorithm (flow networks)
- Minimum Spanning Tree
- Best First Search
- Jump Point Search
- A\* Search Algorithm
- Trigram Search
- Collision Detection
- Line Segment Intersection
- Minimum Bounding Box
- Alpha-beta pruning (or just minimax)
- Ant Colony

Here are some overly broad topic lists.

- [https://en.wikipedia.org/wiki/List_of_data_structures](https://en.wikipedia.org/wiki/List_of_data_structures)
- [https://en.wikipedia.org/wiki/List_of_algorithms](https://en.wikipedia.org/wiki/List_of_algorithms)

### Selection Guidelines

It is easy to select something either too large or too small. The balance is if you end up doing a lot of coding, we will
look more at the code than the report. But if your coding is relatively simple (as single function with a few test
cases), then we will expect a more detailed report/research surrounding it.

Part of programming is often researching the best way to do something. For this assignment, you will be demonstrating your ability
to research and implement an algorithm or data structure.

> Feel free to reach out to ask if something is of the appropriate size! Also feel free to talk about algorithms or data structures in the general channel on MS Teams!!

## Empirical Analysis

You will be providing a detailed analysis of the algorithm or data structure. However, it can also be very difficult to figure out the best way to analyze an algorithm or data structure. We have already shown using HW05 and the Midterm comparison analysis by looking at the speed between algorithms or the speed between various implementations of the same algorithm.

In lab, you have also look at collisions for hash functions, and used that as a means to compare hash functions. There are other ways to look at an analysis also, including documenting the running of the algorithm itself. For example, adding a large number of items to an AVL, and then documenting how many swaps are needed to keep it balanced, and then comparing those swaps to the number of searches operations. Another way is to show the efficiency of the algorithm given a certain dataset size, and then discuss its scalability. For some algorithms, you will find are good at smaller sizes, but they fall into a category called NP or NP-Complete at higher levels. That is fine! You do not need to be trying to solve it for the large cases (those are actually very difficult to solve - and the heart of the discussion in 5800: P vs NP).

We are sure that you can come up with other means such as graphs, visualizations, and more, but the important part is that you are telling us the 'story' behind it in a data driven way. It needs to help you understand the algorithm, and help the reader better understand the algorithm. Yes, an online webpage can be a visualization (if you make one). If you do that, make sure you include it in your report / or at least screen shots of it running. We would consider that part of the analysis even if it isn't an analysis in the traditional sense.

> We suggest you think about this _BEFORE_ you implement the algorithm and feel free to ask for ideas.

## Grading Rubric

Make sure to review this rubric. Additionally, the [README.md](../README.md) provides an outline and guidelines.

### Code (5 points)

- Code is provided (1 point)
- Code is documented (1 point)
  - Code is fully documented with every function documented, and any unusual lines explained (1 point)
- Tests are provided to test algorithm/datastructure (1 point)
- Provided files show a history of tests / information generated for research (1 point)
  - example: if running timings, the file that generated the timings is shown / easy to find.

### Report (12 points)

- Report is easy to read, written at a college level (1 points)
- Report Spelling and grammar are correct (1 point)
- Report provides a history of the algorithm or data structure (1 point)
- Report provides clear examples of the use of the algorithm or data structure (2 points)
- Report provides a discussion of the algorithm or data structure (1 point)
  - Discussion of the implementation of the algorithm or data structure is provided in a way that it can be reproduced. (1 point)
- Report provides mathematical analysis of the algorithm or data structure (1 point)
- Report provides citations (at a minimum of links) for all sources (1 point)
  - Report provides peer reviewed papers as citations (at least 2) related to the algorithm or data structure (1 point)
- Report provides an empirical analysis of the algorithm or data structure (1 point)
  - Empirical analysis is good at demonstrating the algorithm/datastructure. For example, is it a comparison, an analysis of its run / breakdown of the run, etc. (1 point)

Note: the rubic is subject to change as the assignment is refined and improved. Please make sure to double check the most recent revision of the rubric shown in gradescope.
