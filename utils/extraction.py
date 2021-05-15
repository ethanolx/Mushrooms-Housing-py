from typing import Dict
import re

def extract_attributes(metadata: str, target: str) -> Dict[str, Dict[str, str]]:
    '''
    Extract attribute data from ./data/agaricus-lepiota.names file
    '''

    # extract attributes section
    attribute_section = re.findall(target, metadata)[0][0]

    # remove all whitespace
    trimmed_whitespace = re.sub(r'[\s]+', '', attribute_section)

    # split attributes by list numbers
    # remove list numbering
    split_attrs = re.split(r'[\d]+\.', trimmed_whitespace)[1:]

    # attr_dict - final attribute dictionary
    attr_dict = {
        'class': {
            'e': 'edible',
            'p': 'poisonous'
        }
    }
    for attr in split_attrs:
        # attr - raw attribute form
        # e.g. "cap-shape:bell=b,conical=c,convex=x,flat=f,knobbed=k,sunken=s"

        val_dict = {}
        # val_dict - value dictionary for each attribute
        # e.g.
        #   'cap-shape': {
        #       'b': 'bell',
        #       'c': 'conical' ...
        #   }

        name, vals = attr.split(':')
        # name - attribute name
        # e.g. "cap-shape"

        # vals - string of raw attribute pairs
        # e.g. "bell=b,conical=c,convex=x,flat=f,knobbed=k,sunken=s"
        for val in vals.split(','):
            # vals.split(',') - list of raw attribute pairs
            # e.g. ["bell=b", "conical=c", "convex=x", "flat=f", "knobbed=k", "sunken=s"]

            # val - raw attribute pair
            # e.g. "bell=b"
            definition, code = val.split('=')
            # definition - full form of an attribute value
            # e.g. "bell"

            # code - short form of an attribute value
            # e.g. "b"
            val_dict[code] = definition
        attr_dict[name] = val_dict
    return attr_dict