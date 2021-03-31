import json
import logging
import traceback

import {{cookiecutter.base_module_name}}

def lambda_handler(event, context):
    # """Uncomment and create docstring here if you are going to add one"""

    try:
        {{cookiecutter.lambda_name}} = {{cookiecutter.base_module_name}}.{{cookiecutter.base_class_name}}()

        # do work and get outcome

        return {
            "statusCode": 200,
            "body": "Hello World! -- JSON body should go here"
        }
    except Exception as e:
        logger = logging.getLogger(__name__)

        logger.error(traceback.format_exc())

        return {
            "statusCode": 404
        }

    