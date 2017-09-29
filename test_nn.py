import numpy as np

import nn
import datum_reader as datum_reader


def test_make_h():
    v = np.matrix([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])
    i = np.matrix([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]])
    ans = nn.make_h(v, i)
    print(ans)
# test_make_h()
# passed


def test_back_propagate():
    datum = [np.matrix([[.1], [.5], [.9]]),
             np.matrix([.9])]
    alpha = 1
    v = np.matrix([[.5, .5, .5],
                   [.5, .5, .5],
                   [.5, .5, .5],
                   [.5, .5, .5]])
    w = np.matrix([[.5, .5, .5, .5]])
    ans = nn.back_propagate(datum, alpha, v, w)
    print(ans)

# test_back_propagate()
# passed


def test_forward_propagate():
    datum = [np.matrix([[0.4], [0.15], [0.3]]),
             np.matrix([[0.25], [0.25], [0.25], [0.5], [0.25]])]
    v = np.matrix([[0.3, 0.3, 0.3],
                   [0.2, 0.3, 0.4],
                   [0.4, 0.4, 0.5],
                   [0.1, 0.2, 0.3]])
    w = np.matrix([[0.2, 0.1, 0.4, 0.6],
                   [0.2, 0.3, 0.1, 0.2],
                   [0.2, 0.4, 0.4, 0.2],
                   [0.1, 0.3, 0.4, 0.2],
                   [0.1, 0.3, 0.4, 0.2]])
    ans = nn.forward_propagate(datum, v, w)
    print(ans)

# test_forward_propagate()
# passed


def test_normalize():
    data = [[-10, 30, 10],
            [20, 20, 20],
            [25, 25, 25],
            [30, 30, 30]]
    mat = np.matrix(data)
    print(mat)
    norm = datum_reader.normalize_data(mat)
    print(norm)

# test_normalize()
# passed


def test_build_network():
    print("reading data...")
    data = datum_reader.read_in_data_csv_with_class_last(
        "DataSets/winequality-white.csv", ";")
    data = datum_reader.normalize_data(np.matrix(data))
    num_hidden_units = 15
    alpha = 5
    initial_bounds = 1000
    max_iterations = 3
    modulo = 1
    print("building net...")
    ans = nn.build_network(data, num_hidden_units, alpha,
                           initial_bounds, max_iterations, modulo)
    print("  complete.")
    print(ans)

# test_build_network()


wine = datum_reader.normalize_file(
    "DataSets/winequality-white.csv", ";")
