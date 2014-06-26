#!/usr/bin/env python

import yaml
import json
import sys

try:
    in_file = sys.argv[1]
except:
    print "Must provide a YAML file to convert"

with open(in_file) as _in:
    obj = yaml.load(_in)
    print json.dumps(obj, indent=4)
