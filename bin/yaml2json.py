#!/usr/bin/env python

try:
    import yaml
except ImportError:
    raise SystemExit("Could not locate python YAML library. Please install PyYAML to continue")

try:
    import json
except ImportError:
    raise SystemExit("Could not locate python JSON library. Please install python-simplejson to continue")

import sys

try:
    in_file = sys.argv[1]
except:
    raise SystemExit("Must provide a YAML file to convert as an argument to this script")

with open(in_file) as _in:
    obj = yaml.load(_in)
    print json.dumps(obj, indent=4)
