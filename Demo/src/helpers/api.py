import json
import logging

"""
Functions for handling API conversion
"""

def attributes(data):
    """ 
    Convert attributes dictiony into API format 
    Expecting a defaultdict(dict) of keys "boolean", "date", "double", "string"
    Returns a list of dictionaries such as {"type": mode, "name": name, "value": value}
    """
    result = [] 
    
    for mode in ("boolean", "date", "double", "string"):
        fields = data[mode]
        for attribute in fields: 
            value = fields[attribute]
            
            if value or value == False:
                build = {"type": mode, "name": attribute, "value": value}
                result.append(build)
            else:
                logging.debug(f"Empty value mode: {mode}, name: {attribute}")
                continue
    return result 


def entities(data):  
    """ 
    Convert entities dictionary into API format 
    Expecting a dictionary containing roles and their associated entity 
    Returns a list of dictionaries such as {"role": role, "entities": entity}
    """
    result = []
    for role, entity in data.items():
        if entity:
            result.append({"role": role, "entities": entity})
    return result

