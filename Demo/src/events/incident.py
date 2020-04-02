from collections import defaultdict
from .event import Event
from ..helpers.descriptors import Database, Dates

class Incident(Event):
    """ 
    Base Class for required fields 
    Not to be used directly, but inherited as an example base set of fields and rules
    """
    
    description = Database()
    incident_date = Dates()
            
    def __init__(self, first_name, last_name, incident_date, source, description):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.incident_date = incident_date
        self.source = source
        self.description = description
        
    @property
    def attributes(self):
        """Attribute fields for event"""
        attr = defaultdict(dict)   
        attr["date"] = {"Incident Date": self.incident_date}
        attr["string"] = {"First Name": self.first_name,
                          "Last Name": self.last_name,
                          "Source": self.source}
        return attr
    
    @property
    def entities(self):
        ent = {}
        ent["Primary"] = f"{self.first_name} {self.last_name}"
        return ent

    @property
    def content(self):
        return self.description 
    
    @property 
    def mode(self):
        return self.source