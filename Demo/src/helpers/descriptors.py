import datetime
import logging

class Descript(object):
    """Parent"""
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Booleans(Descript):
    """Class for converting logical yes items into boolean True"""
    def __set__(self, instance, value):
        if value.lower().strip() in ('true', 't', 'yes', 'y'):
            instance.__dict__[self.name] = True
        else:
            instance.__dict__[self.name] = False
            
            
class Database(Descript):
    """lookup value from a fake database..."""
    def __set__(self, instance, value):
        codes = {"11": "Data Exfiltration",
                 "22": "Brute Force Attempt",
                 "33": "Unauthorized Physical Access",
                 "44": "Off Hours Badge Scan"}        
        # Imagine this is calling a database instead... 
        instance.__dict__[self.name] = codes.get(value.strip(), "Unavailable Value")


class Dates(Descript):
    """Convert date to iso format"""
    def __set__(self, instance, value):
        for fmt in ('%m/%d/%y', '%m/%d/%Y', '%b-%y', '%b-%Y', '%d-%b-%y', '%d-%b-%Y'):
            try:
                value = datetime.datetime.strptime(value, fmt).isoformat()
                break
            except: 
                pass
        else: 
            logging.debug(f"Unable to convert {value} to datetime")
            value = None
        instance.__dict__[self.name] = value
                          
