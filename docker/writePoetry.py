#!/bin/env python

# On the first day...
# That's right, for Halloween!

# Vanessa Sochat @vsoch
# October 31, 2018
# Happy Halloweenie!

import os
import re
import requests
import sys
import yaml
import random
from generate import RobotNamer

## Helper Functions


# Yaml

def read_yaml(section, quiet=False):
    '''read yaml from a string, either read from file (read_frontmatter) or 
       from yml file proper (read_yaml)

       Parameters
       ==========
       section: a string of unparsed yaml content.
    '''
    metadata = {}
    docs = yaml.load_all(section)
    for doc in docs:
        if isinstance(doc, dict):
            for k,v in doc.items():
                if not quiet:
                    print('%s: %s' %(k,v))
                metadata[k] = v
    return metadata


def generate_lookup(thing):
    '''convert of list of dicts to a single dict. I know, I know.
    '''
    lookup = dict()
    [lookup.update(item) for item in thing]
    return lookup


def get_things():
    '''Retrieve the online things.yml from Github
    '''
    repo_base = "https://raw.githubusercontent.com/vsoch/40-avocados"
    url = "%s/master/things.yml" % repo_base
    response = requests.get(url)
    if response.status_code == 200:
        return read_yaml(response.text, quiet=True)

def get_prefix(item):
    '''get the correct prefix depending on the first letter. Return "an" for
       vowels, a otherwise

       Parameters
       ==========
       item: the name of the item to get a prefix for
    '''
    prefix = 'a'
    if re.search('^(a|e|i|o|u)', item):
        prefix = 'an'
    return prefix


# Write Poetry

def get_beloved():
    bot = RobotNamer()
    return bot.generate()

def get_day():
    choices = ['Halloweenie', 'Hacktoberfest', 'October', 'Fall', 'Halloween']
    return random.choice(choices)

def get_item(choice, lookup, write_markdown, add_prefix=False):
    item = random.choice(lookup[choice])

    # Should we add a prefix? (Only the last one)
    if add_prefix:
        choice = get_prefix(item)
    name = "%s %s" % (choice, item.replace('-', ' '))

    if write_markdown:
        item = "[%s](https://vsoch.github.io/40-avocados/%s)" %(name, item)
    return item

def print_line(line, write_markdown):
    if write_markdown:
        line = " - %s" % line
    print(line)


def writePoem(lookup, write_markdown=False):
    '''given a lookup where keys are numbers of things and values are lsits
       of things, write a "12 Days of Christmas" type of poem and print to the
       screen.

       Parameters
       ==========
       lookup: keys are integers (counts of things) values are lists of things
       numbers: a corresponding list 
       write_markdown: if True, include link to item
    '''
    numbers = list(lookup.keys())

    # Write the poem! Sort the dictionary by number
    numbers.sort()
        
    # Iterate through 12 times, choose a random number, always start with 1
    choices = [1]
    while len(choices) < 12:
        choice = random.choice(numbers)
        if choice not in choices:
            choices.append(choice)
    choices.sort()

    # Write the poem! Leave 1 in the list
    while len(choices) > 1:    

        # Select a number
        choice = choices.pop()

        # Get your beloved
        beloved = get_beloved()            
        item = get_item(choice, lookup, write_markdown)
        day = get_day()
        
        line = 'On the %s day of %s my %s gave to me, ... %s' %(choice, day,
                                                               beloved, item)
        print_line(line, write_markdown)

                

    # Always a 1!
    choice = choices.pop()
    item = get_item(choice, lookup, write_markdown, add_prefix=True)   

    line = 'And %s just for me :)' %(item)
    print_line(line, write_markdown)



def main(write_markdown=False):

    # 1. Read in the things.yml file
    things = get_things()

    # Generate lookup based on name
    lookup = dict()

    for name,thing in things['things'].items():

        thing = generate_lookup(thing)

        # 3. Add the number
        number = int(thing.get("number", 40))
        number = max(number, 1)

        # Add to lookup based on number
        if number not in lookup:
            lookup[number] = []
        lookup[number].append(name)


    writePoem(lookup, write_markdown)
    
if __name__ == '__main__':
    write_markdown = False
    if len(sys.argv) > 1:
        write_markdown = True
    main(write_markdown)
