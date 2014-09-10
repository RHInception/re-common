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

def _decode_list(data):
    rv = []
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        elif isinstance(item, list):
            item = _decode_list(item)
        elif isinstance(item, dict):
            item = _decode_dict(item)
        rv.append(item)
    return rv

def _decode_dict(data):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        elif isinstance(value, list):
            value = _decode_list(value)
        elif isinstance(value, dict):
            value = _decode_dict(value)
        rv[key] = value
    return rv

with open(in_file) as _in:
    obj = json.load(_in, object_hook=_decode_dict)
    print yaml.dump(obj)
