#!/usr/bin/env python
from pprint import pprint as pp
import argparse
import sys
import os
import jsonschema
from jsonschema import Draft4Validator
import json

schema_dir = 'schemas'
test_dir = 'test-documents'

schemas = os.listdir(schema_dir)
test_docs = os.listdir(test_dir)

schema_validation_results = {}
test_map = {}

for test_doc in test_docs:
    print "Trying to find a schema for %s" % test_doc

    for schema in schemas:
        schema_basename = schema.replace('.json', '')
        # print "--- evaluating %s" % schema_basename

        if test_doc.startswith(schema_basename):
            # print "--- SCHEMA DISCOVERED: Validating %s with %s" % (
            #     test_doc, schema_basename)
            test_map[test_doc] = schema
            break

def validate_schemas():
    for schema in schemas:
        print ">>> Validating schema: %s" % schema
        valid = False
        try:
            with open(os.path.join(schema_dir, schema), 'r') as schema_fp:
                s = json.loads(schema_fp.read())
            Draft4Validator.check_schema(s)
        except Exception, e:
            print ">>> %s: FAILED" % schema
            print e
        else:
            print ">>> %s: PASSED" % schema
            valid = True

        schema_validation_results[schema] = valid
        print """
"""


    pp(schema_validation_results)


# for doc, schema in test_map.iteritems():

print """




"""
validate_schemas()
