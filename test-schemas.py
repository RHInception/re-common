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



BG = {}
BG['BLACK'] = '\033[40m'
BG['RED'] = '\033[41m'
BG['GREEN'] = '\033[42m'
BG['YELLOW'] = '\033[43m'
BG['BLUE'] = '\033[44m'
BG['PURPLE'] = '\033[45m'
BG['CYAN'] = '\033[46m'
BG['LIGHTGRAY'] = '\033[47m'
COLORS = {}
COLORS['RESTORE'] = '\033[0m'
COLORS['RED'] = '\033[00;31m'
COLORS['GREEN'] = '\033[00;32m'
COLORS['YELLOW'] = '\033[00;33m'
COLORS['BLUE'] = '\033[00;34m'
COLORS['PURPLE'] = '\033[00;35m'
COLORS['CYAN'] = '\033[00;36m'
COLORS['TEAL'] = '\033[00;36m'
COLORS['LIGHTGRAY'] = '\033[00;37m'
COLORS['LRED'] = '\033[01;31m'
COLORS['LGREEN'] = '\033[01;32m'
COLORS['LYELLOW'] = '\033[01;33m'
COLORS['LBLUE'] = '\033[01;34m'
COLORS['LPURPLE'] = '\033[01;35m'
COLORS['LCYAN'] = '\033[01;36m'
COLORS['WHITE'] = '\033[01;37m'


def colorize(item, color=None, underline=False, background=None):
    if underline:
        ul = "\033[4m"
    else:
        ul = ''

    if background:
        bg = BG[background.upper()]
    else:
        bg = ""

    if color:
        c = COLORS[color.upper()]
    else:
        c = COLORS["WHITE"]

    return "%s%s%s%s%s%s" % (COLORS['RESTORE'],
                             c,
                             bg, ul, item,
                             COLORS['RESTORE'])


def build_test_map():
    print colorize("Building document -> schema test mapping...", color="yellow")
    print ""
    test_map = {}
    for test_doc in test_docs:
        # print "Trying to find a schema for %s" % test_doc

        for schema in schemas:
            schema_basename = schema.replace('.json', '')
            # print "--- evaluating %s" % schema_basename

            if test_doc.startswith(schema_basename):
                # print "--- SCHEMA DISCOVERED: Validating %s with %s" % (
                #     test_doc, schema_basename)
                test_map[test_doc] = schema
                break
    return test_map

def validate_schemas():
    print colorize("Validating each schema...", color="yellow")
    schema_validation_results = {}
    for schema in schemas:
        # print ">>> Validating schema: %s" % schema
        valid = False
        try:
            with open(os.path.join(schema_dir, schema), 'r') as schema_fp:
                s = json.loads(schema_fp.read())
            Draft4Validator.check_schema(s)
        except Exception, e:
            print ">>> %s: FAILED" % schema

            print e
            print ""
        else:
            #print ">>> %s: PASSED" % schema
            valid = True

        schema_validation_results[schema] = valid

    return schema_validation_results


def validate_test_documents():
    print colorize("Validating each test document...", color="yellow")
    document_validation_results = {}
    for doc, schema in test_map.iteritems():
#        print "Validating document %s using %s schema" % (doc, schema)

        valid = False
        try:
            with open(os.path.join(test_dir, doc), 'r') as test_doc_fp:
                test_doc = json.loads(test_doc_fp.read())

            with open(os.path.join(schema_dir, schema), 'r') as test_schema_fp:
                test_schema = json.loads(test_schema_fp.read())

            jsonschema.validate(test_doc, test_schema)
        except Exception, e:
            print "----------------------------------------------------------------------------------"
            print "Error while validating document: %s with %s" % (doc, schema)
            print e
        else:
            valid = True

        document_validation_results[doc] = valid

    return document_validation_results

test_map = build_test_map()
schema_validation_results = validate_schemas()

print colorize("Schema Validation Results:", color="cyan")
for k, v in schema_validation_results.iteritems():
    if v:
        result = "PASSED"
        color = "green"
    else:
        result = "FAILED"
        color = "red"
    print "%s: %s" % (
        k, colorize(result, color=color))


print ""

document_validation_results = validate_test_documents()
print colorize("Document Validation Results:", color="cyan")
for k, v in document_validation_results.iteritems():
    if v:
        result = "PASSED"
        color = "green"
    else:
        result = "FAILED"
        color = "red"
    print "%s: %s" % (
        k, colorize(result, color=color))
