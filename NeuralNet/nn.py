# Two later back-progapagaion Neural Network
# a datum is an array of 2 items, datapoints (index 0) and the class (index 1)


import numpy as np


def shuffle(list):
    # randomize a list
    return list


def sigmoid(u):
    ans = 1 / (1 + (np.exp(-u)))
    return ans


def sigmoid_matrix(mat):
    # calls sigmoid on each element in the matrix
    sig = np.vectorize(sigmoid)
    ans = sig(mat)
    return ans

# returns (as a scalar) the error between the output and correct vectors


def net_error(o, c):
    # error = 0.5 * (transpose(c-o) . (c-o))
    diff = np.subtract(c, o)
    dot = diff.transpose().dot(diff)
    ans = np.multiply(0.5, dot)
    return ans

# makes matrix filled randomly with -val to val


def gen_random_matrix(i, j, val):
    if(i <= 0 or j <= 0):
        return [0]
    mat = (2 * val * np.random.random_sample((i, j))) - val
    return mat


# I know these two functions are redundant, but it helps readability
def make_h(v, i):
    ans = sigmoid_matrix(v.dot(i))
    return ans


def make_o(w, h):
    ans = sigmoid_matrix(w.dot(h))
    return ans


def forward_propagate(datum, v, w):
    h = make_h(v, datum[0])
    o = make_o(w, h)
    return o


def back_propagate(datum, alpha, v, w):
    # i is (first datum)
    # c is (second datum)
    # h = sigmoid[v . i]
    # o = sigmoid[w . h]
    # odelta = (c - o) * o * (1 - o)
    # hdelta = (h * (1 - h) * (tr[w] . odelta))
    # wdelta = alpha % (odelta . tr[h])
    # vdelta = alpha (hdelta . tr[i])
    # returns a list of (w + wdelta) and (v + vdelta)
    # which are updated network matricies
    i = datum[0]
    c = datum[1]
    h = make_h(v, i)
    o = make_o(w, h)
    odelta = np.multiply(np.multiply((c - o), o), (1 - o))
    hdelta = np.multiply(np.multiply(h, (1 - h)),
                         w.transpose().dot(odelta))
    wdelta = np.multiply(alpha, odelta.dot(h.transpose()))
    vdelta = np.multiply(alpha, hdelta.dot(i.transpose()))
    ans = ((v + vdelta), (w + wdelta))
    return ans

# returns the learned network matricies
# data - array of datums


def build_network(data, num_hidden_units, alpha,
                  initial_bounds, max_iterations, modulo):
    a_good_min_error = 1.0e-9
    i = len(data[0][1])  # number of outputs, 0th data point's output
    j = num_hidden_units
    k = len(data[0][0])  # number of inputs, 0th data point's input
    v = gen_random_matrix(j, k, initial_bounds)  # input weights
    w = gen_random_matrix(i, j, initial_bounds)  # output weights

    for i in range(max_iterations):
        # For each data element in a randomized version of the data,
        # perform backpropagation.
        v = 0
        w = 0
        for datum in shuffle(data):
            (v, w) = back_propagate(datum, alpha, v, w)

        # every modulo iterations
        if i % modulo == 0:
            # For every data element in the data, perform forward
            # propagation and collecting all the errors from
            # forward_propagate and throwing them in a list
            errors_all = list(map(
                lambda datum:
                    net_error(
                        forward_propagate(datum, v, w),
                        datum[1]),
                data))
            error_worst = np.max(errors_all)
            print(error_worst)
            # errors_mean = np.average(errors_all)

            if(error_worst < a_good_min_error):
                print("breaking out the of the loop with a min error of: %f" %
                      error_worst)
                break
    return v, w
