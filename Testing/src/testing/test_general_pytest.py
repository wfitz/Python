import pytest

@pytest.mark.skip(reason="Comment out for example")
def test_long_string_display():
    string = ("See what happens with a potentially very long, long, string in this text area...")
    expected = ("See what happens with a potentially very long, long string in this text area...")
    assert string == expected