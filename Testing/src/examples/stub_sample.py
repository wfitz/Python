def return_aliases(entity):
    """
    Return list of aliases for an entity
    """
    raw_entity = query_database(entity)
    
    result = []
    for alias in raw_entity.get("aliases", ""):
        result.append(alias["alias"])
    return result
    
    
def query_database(entity):
    """
    Return raw json for an entity from database 
    """
    print("connecting to database...")
    return {"info": "fake"}