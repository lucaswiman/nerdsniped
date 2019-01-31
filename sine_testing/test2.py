from hypothesis import given
import hypothesis.strategies as st
π = 3.1415

@given(st.floats(min_value=-π, max_value=π).filter(lambda x: abs(x) > 1e-5))
def test_foo(bar):
    pass