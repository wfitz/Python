from __future__ import absolute_import

import pytest
from src.examples.coding import division
#from hypothesis import given, assume, strategies as st

def test_division_with_two_ints():
    """Test a couple known good cases"""
    assert division(2,4) == .5
    assert division(1,3) == pytest.approx(.333, .1)
    

@pytest.mark.this
def test_division_wrong_type_string():
    """Verify TypeError with string value"""
    with pytest.raises(TypeError):
        division(4, "2")

        
#@given(st.integers(), st.integers())
#def test_with_hypothesis_ints(num, denom):
#    """Stress test for potential errors"""
#    assume(denom > 0) 
#    division(num, denom)