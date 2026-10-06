# matrix-eigenvalues-pagerank
# Matrix Eigenvalues and Google's PageRank Algorithm

A mathematical and computational study of eigenvalues, eigenvectors, and Google's PageRank algorithm.

## Project Overview

PageRank is a link-analysis algorithm that ranks web pages based on the structure of links between them. This project studies the mathematical foundation of PageRank using matrix operations, eigenvalues, and eigenvectors.

The project implements PageRank in Python and demonstrates two approaches:

1. **Eigenvector method** — PageRank is obtained from the eigenvector corresponding to eigenvalue 1 of the Google matrix.
2. **Power iteration method** — PageRank is obtained iteratively using repeated matrix-vector multiplication.

The implementations are verified using numerical checks and compared with NetworkX.

## Mathematical Foundation

A directed web graph is represented using an adjacency matrix \(A\).

From this, a column-stochastic transition matrix \(M\) is constructed:

\[
M_{ij} = P(\text{page }j \rightarrow \text{page }i)
\]

Dangling pages, which have no outgoing links, are assigned a uniform probability distribution.

The Google matrix is then constructed as:

\[
G = dM + (1-d)\frac{1}{N}E
\]

where:

- \(d\) is the damping factor, typically \(0.85\)
- \(N\) is the number of pages
- \(E\) is an \(N\times N\) matrix of ones

The PageRank vector \(PR\) satisfies:

\[
GPR = PR
\]

Therefore, PageRank is the normalized eigenvector corresponding to the eigenvalue:

\[
\lambda = 1
\]

### Power Iteration

The same PageRank vector can be obtained iteratively:

\[
PR^{(k+1)} = GPR^{(k)}
\]

The iteration continues until the difference between successive PageRank vectors falls below a specified tolerance.

## Project Pipeline

```text
Directed Graph
      ↓
Adjacency Matrix A
      ↓
Transition Matrix M
      ↓
Google Matrix G
      ↓
 ┌───────────────┐
 │               │
Eigenvector   Power Iteration
 │               │
 └───────┬───────┘
         ↓
     PageRank
         ↓
   Verification
