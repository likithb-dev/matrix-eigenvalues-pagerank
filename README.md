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

## Pipeline

```mermaid
flowchart TD
    A["Directed graph<br/>(web pages and links)"] --> B["Adjacency matrix A"]
    B --> C["Transition matrix M<br/>(column-stochastic)"]
    C --> D["Google matrix G<br/>(damping + teleportation)"]
    D --> E["Method 1: Eigenvector<br/>solve G r = r"]
    D --> F["Method 2: Power iteration<br/>r ← G r until convergence"]
    E --> G["PageRank vector r"]
    F --> G
    G --> H["Verification<br/>(cross-check both methods)"]
```

## What each stage does

| Stage | Object | Definition |
|---|---|---|
| 1. Graph | Directed graph with $n$ nodes | Edge $j \to i$ means page $j$ links to page $i$ |
| 2. Adjacency | $A \in \{0,1\}^{n \times n}$ | $A_{ij} = 1$ if $j \to i$ (so column $j$ lists the outlinks of $j$) |
| 3. Transition | $M$ | $M_{ij} = A_{ij} / \text{outdeg}(j)$, so every column sums to 1. Dangling nodes (no outlinks) get a uniform column $1/n$ |
| 4. Google matrix | $G$ | $G = \alpha M + (1-\alpha)\frac{1}{n}\mathbf{1}\mathbf{1}^T$, with damping $\alpha = 0.85$ |
| 5a. Eigenvector | $G r = r$ | $r$ is the eigenvector for eigenvalue $\lambda = 1$, normalized so $\sum r_i = 1$ |
| 5b. Power iteration | $r_{k+1} = G r_k$ | Start from $r_0 = \frac{1}{n}\mathbf{1}$; stop when $\lVert r_{k+1} - r_k \rVert_1 < \varepsilon$ |
| 6. Verification | Consistency checks | See below |

## Verification checks

1. $\sum_i r_i = 1$ and all $r_i > 0$
2. Residual $\lVert G r - r \rVert_1 \approx 0$
3. Eigenvector result and power-iteration result agree within tolerance
4. Ranking matches `networkx.pagerank(G, alpha=0.85)`
