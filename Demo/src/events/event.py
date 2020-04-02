import datetime
from ..helpers import api

"""
Sample example class used to build json format for posting to an API 
Inhert this class to new schemas and override fields as needed
"""

class Event():
    
    """Base Class for posting to example json API"""
    def __repr__(self):
        """Print out class variables and values for debug"""
        return '\n'.join(f"{key}: {vars(self)[key]}" for key in sorted(vars(self)))
        
    @property
    def attributes(self):
        pass
    
    @property
    def content(self):
        pass

    @property 
    def entities(self):
        pass
    
    @property 
    def mode(self):
        pass
    
    @property
    def timestamp(self):
        """Returns current time in ISO format by default"""
        return datetime.datetime.utcnow().isoformat()
    
    @property
    def output(self):
        """Convert data to json for posting to API"""
        event = {}
        
        for field in ("content", "mode", "timestamp"):
            value = getattr(self, field)
            if value:
                event[field] = value
                
        for field in ("attributes", "entities"):
            func = getattr(api, field)
            value = getattr(self, field)
            if value:
                event[field] = func(value)
        return event