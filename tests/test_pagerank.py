import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from pagerank import build_transition_matrix, build_google_matrix
from power_iteration import pagerank, eigen_check


def test_transition_matrix_columns_sum_to_one():
    nodes = ["A", "B", "C", "D"]

    edges = [
        ("A", "B"),
        ("A", "C"),
        ("B", "C"),
        ("C", "A"),
        ("C", "D"),
        ("D", "A")
    ]

    M = build_transition_matrix(nodes, edges)

    assert np.allclose(M.sum(axis=0), 1.0)


def test_dangling_node_gets_uniform_probability():
    nodes = ["A", "B", "C"]

    edges = [
        ("A", "B"),
        ("B", "C")
    ]

    M = build_transition_matrix(nodes, edges)

    # C is a dangling node, so its column should be uniform.
    assert np.allclose(M[:, 2], [1 / 3, 1 / 3, 1 / 3])


def test_pagerank_sums_to_one():
    A = np.array([
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 0]
    ], dtype=float)

    pr, history, G = pagerank(A)

    assert np.isclose(pr.sum(), 1.0)


def test_pagerank_is_eigenvector():
    A = np.array([
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 0]
    ], dtype=float)

    pr, history, G = pagerank(A)

    checks = eigen_check(G, pr)

    assert checks["sums_to_1"]
    assert checks["columns_sum_to_1"]
    assert checks["residual ||G@pr - pr||_1"] < 1e-8