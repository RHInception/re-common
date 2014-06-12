RELEASE ENGINE COMMON
---------------------

This repository holds shared (common) items utilized by several of the Release Engine components.

For more documentation see the
[Read The Docs](http://release-engine.readthedocs.org/en/latest/components/recore.html)
documentation.


Running the Tests
-----------------

    $ ./test-schemas.py
    Schema Validity:
    {'playbook_schema.json': True,
     'recore_deployment.json': True,
     'rerest_deployment.json': True,
     'rerest_deployment_response.json': True,
     'reworker_deployment_status.json': True}

    Document Validity:
    {'playbook_schema_valid.json': True,
     'recore_deployment_argument_notify_valid.json': True,
     'recore_deployment_argument_valid.json': True,
     'recore_deployment_dynamic_valid.json': True,
     'recore_deployment_simple.json': True,
     'rerest_deployment_dynamic_valid.json': True,
     'rerest_deployment_response_failed_valid.json': True,
     'rerest_deployment_response_success_valid.json': True,
     'rerest_deployment_simple_valid.json': True,
     'reworker_deployment_status_completed_valid.json': True,
     'reworker_deployment_status_failed_valid.json': True,
     'reworker_deployment_status_started_valid.json': True}

Any errors will be spit out at run-time.
