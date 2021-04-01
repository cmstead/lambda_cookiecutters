import json
# import approvaltests

from lambda_source import {{cookiecutter.base_module_name}}




def test_{{cookiecutter.lambda_name|lower}}_{{cookiecutter.http_method|lower}}():
    {{cookiecutter.lambda_name}} = {{cookiecutter.base_module_name}}.{{cookiecutter.base_class_name}}()

    # Do work here

    assert False == True