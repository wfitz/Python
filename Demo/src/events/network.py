from collections import defaultdict
from .incident import Incident
from ..helpers.descriptors import Booleans
        
class Network(Incident):
    """ 
    Network incident example 
    Inherits from Incident to get base rulesets
    """
    
    flagged = Booleans()
    
    def __init__(self, *args):
        *base, flag = args
        super().__init__(*base)
        self.flagged = flag
        
    @property
    def attributes(self):
        """ Update attributes """
        attr = super().attributes
        attr["boolean"].update({"Flagged": self.flagged})
        return attr