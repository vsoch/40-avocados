#!/bin/env python

# Generate 40 things.
# Vanessa Sochat @vsoch
# October 30, 2018
# Halloweenie!

import os
import requests
import sys
import yaml

## Helper Functions

def read_file(filename, mode="r", readlines=True):
    '''write_file will open a file, "filename" and write content, "content"
       and properly close the file
    '''
    with open(filename, mode) as filey:
        if readlines is True:
            content = filey.readlines()
        else:
            content = filey.read()
    return content


def write_file(filename, content, mode="w"):
    '''write_file will open a file, "filename" and write content, "content"
       and properly close the file
    '''
    with open(filename, mode) as filey:
        filey.writelines(content)
    return filename


# Yaml

def read_yaml(filename, mode='r', quiet=False):
    '''read a yaml file, only including sections between dashes
    '''
    stream = read_file(filename, mode, readlines=False)
    return _read_yaml(stream, quiet=quiet)


def write_yaml(yaml_dict, filename, mode="w"):
    '''write a dictionary to yaml file
 
       Parameters
       ==========
       yaml_dict: the dict to print to yaml
       filename: the output file to write to
       pretty_print: if True, will use nicer formatting
    '''
    with open(filename, mode) as filey:
        filey.writelines(yaml.dump(yaml_dict))
    return filename

   
def _read_yaml(section, quiet=False):
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


## Generation

def generate_grid(image, url, number=40):
    '''generate the grid, meaning the grid-item classes to embed some
       number of times.

       Parameters
       ==========
       image: the image url to put in img src
       number: the number of grid-items to produce of the image
       url: the url for the grid-item to link to.
    '''
    elements = []
    element = '<div class="grid-item"><a href="%s"><img src="%s"/></a></div>' %(url, image)
    for i in range(number):
        elements.append(element)
    return '\n'.join(elements)

def generate_lookup(thing):
    '''convert of list of dicts to a single dict. I know, I know.
    '''
    lookup = dict()
    [lookup.update(item) for item in thing]
    return lookup


def generate_html(file_name, template_file, subs):
    '''write the grid html content to a file_name

       Parameters
       ==========
       file_name the name to write of the file, folder must exist
       subs: a dictionary of subs, where key is the template string, value 
             is the content to fill in.
    '''
    template = read_file(template_file, readlines=False)
    for key, content in subs.items():
        template = template.replace("{{ %s }}" % key, str(content))

    # 5. Write template
    write_file(file_name, template)
    return file_name


def main(yaml_file, output_dir, template_file):

    # 1. Read in the things.yml file
    data = read_yaml(yaml_file)

    # 2. Generate a page per thing

    for name,thing in data['things'].items():

        print('Generating %s!' % name)
        thing = generate_lookup(thing)

        # 3. Metadata and Image
        number = int(thing.get("number", 40))

        # Number must be greater than or equal to 1
        number = max(number, 1)
        url = thing.get('link', "https://vsoch.github.io/40-avocados/")
        image = thing.get('image')

        # Test that image is defined
        if image is None:
            print('Missing image definition for %s in things.yml.' % name)
            sys.exit(1)

        # Test that image exists
        if requests.head(image).status_code != 200:
            print('Error with %s, image status not 200!.' % name)
            sys.exit(1)

        # 4. Fill Template
        print("Generating grid...")
        grid = generate_grid(image, url, number)
        file_name = '%s/%s/index.html' % (output_dir, name.lower())
        os.mkdir(os.path.dirname(file_name))

        # 5. Write file
        generate_html(file_name, 
                      template_file, {"kind": name,
                                      "text": "%s %s" %(number, name),
                                      "grid": grid,
                                      "number": number}) 


    # Finally, an index.html. Redundant, yes, I'm tired
    grid = ''
    
    for name,thing in data['things'].items():
        url = "https://vsoch.github.io/40-avocados/%s" % name.lower()
        thing = generate_lookup(thing)
        image = thing.get('image')
        grid += generate_grid(image, url, 1)
        grid += "\n"

    text = "What can I get for $40.00?"
    generate_html('%s/index.html' % output_dir, template_file, {"text": text,
                                                                "grid": grid,
                                                                "number": "This Many",
                                                                "kind": "Things"}) 


if __name__ == '__main__':

    # Hacky input parsing!
    yaml_file = os.path.abspath(sys.argv[1])
    output_dir = os.path.abspath(sys.argv[2])
    template_file = os.path.abspath(sys.argv[3])
    main(yaml_file, output_dir, template_file)
