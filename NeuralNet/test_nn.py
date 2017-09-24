import numpy as np
import nn

def test_forward_propagate():
    datum = [np.matrix([0.4, 0.15, 0.3]), np.matrix([0.25, 0.25, 0.25, 0.5, 0.25])] #[input, output]
    v = np.matrix([[0.3,0.3,0.3], [0.2,0.3,0.4], [0.4,0.4,0.5], [0.1,0.2,0.3]])
    w = np.matrix([[0.2,0.1,0.4,0.6],[0.2,0.3,0.1,0.2],[0.2,0.4,0.4,0.2],[0.1,0.3,0.4,0.2],[0.1,0.3,0.4,0.2]])
    ans = nn.forward_propagate(datum, v, w)
    print ans

test_forward_propagate()