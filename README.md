RELEASE ENGINE COMMON
---------------------

This repository holds shared (common) items utilized by several of the Release Engine components.

For more documentation see the
[Read The Docs](http://release-engine.readthedocs.org/en/latest/components/recore.html)
documentation.


Testing A New Playbook
----------------------

Say you want to test a new playbook. You must name your test playbook
so that it begins with ``playbook``. Also, it must be a **json** file
(use ``yaml2json.py`` if you have a YAML file).

    $ cp my_playbook.json documents/playbook_test.json
	$ ./test-schemas.py


Running the Tests
-----------------

    $ ./test-schemas.py
    Building document -> schema test mapping...

    Validating each schema...
    Schema Validation Results:
    reworker_deployment_status.json: PASSED
    rerest_response_deployment.json: PASSED
    recore_deployment.json: PASSED
    rerest_deployment.json: PASSED
    notification.json: PASSED
    playbooks.json: PASSED

    Validating each test document...
    Document Validation Results:
    rerest_deployment_simple_valid.json: PASSED
    notification_valid.json: PASSED
    rerest_deployment_dynamic_valid.json: PASSED
    recore_deployment_argument_notify_valid.json: PASSED
    reworker_deployment_status_started_valid.json: PASSED
    recore_deployment_argument_valid.json: PASSED
    rerest_response_deployment_success_valid.json: PASSED
    reworker_deployment_status_completed_valid.json: PASSED
    rerest_response_deployment_failed_valid.json: PASSED
    recore_deployment_simple.json: PASSED
    recore_deployment_dynamic_valid.json: PASSED
    reworker_deployment_status_failed_valid.json: PASSED
[
Any errors will be spit out at run-time.
