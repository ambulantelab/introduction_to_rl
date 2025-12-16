import numpy as np
from algorithms.policy_gradient import SoftMaxPolicy

def test_softmax_probs_sum_to_one():
    p = SoftMaxPolicy(3, 2)
    probs = p.probs(0)
    assert np.isclose(np.sum(probs), 1.0)