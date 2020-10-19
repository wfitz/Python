from src.examples.stub_sample import return_aliases
from unittest.mock import patch

def test_return_aliases_with_stub_conftest():
    """Test return alisases given mocked database call"""
    assert return_aliases("entity") == ["Matthewtbaron", "matthewtbaron@emailaddress.com"]   

    
def test_return_aliases_with_stub_empty_json():
    """Test case when None is returned"""
    with patch('src.examples.stub_sample.query_database', return_value={"Response": "Error"}) as qdb:
        assert return_aliases("entity") == []
        