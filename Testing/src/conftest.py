import pytest 
#from unittest.mock import patch
#
#sample_entity = {'id': '0160aee2-46cd-4d45-8c8d-3d05e88ea5ae',
#          'aliases': [{'id': '99c297dc-fe16-496e-9700-d41ee03d5425',
#                       'alias': 'Matthewtbaron',
#                       'type': 'string',
#                       'source': 'SYSTEM_DEFAULT'},
#                      {'id': '16999e57-f8fe-490d-a341-c291e81471e4',
#                       'alias': 'matthewtbaron@emailaddress.com',
#                       'type': 'string',
#                       'source': 'SYSTEM_DEFAULT'}],
#          'attributes': [{'type': 'boolean',
#                          'key': 'Monitored Entity',
#                          'value': 'true'},
#                         {'type': 'double',
#                          'key': 'Risk Level',
#                          'start': '2020-07-30T11:59:59.999Z',
#                          'value': '1.0'}],
#          'actor_id': 'Matthewtbaron',
#          'entity_source': 'SYSTEM_DEFAULT'}
#
#@pytest.fixture(autouse=True)
#def stub_database_entity():
#    """Patch any calls to entity database and return a sample"""
#    with patch('src.examples.stub_sample.query_database', return_value=sample_entity) as qdb:
#        yield qdb
#
#        
#@pytest.fixture()
#def another_fixture():
#    return 42