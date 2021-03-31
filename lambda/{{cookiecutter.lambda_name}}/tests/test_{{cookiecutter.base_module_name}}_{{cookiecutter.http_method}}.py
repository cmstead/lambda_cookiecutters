import json
# import approvaltests

from lambda_source import {{cookiecutter.base_module_name}}

class WdmFake:    
    def __init__(self) -> None:
        pass

    queries = []
    parameters = []

    output_data = []

    def add_output_data(self, data):
        self.output_data.append(data)

    def run_query(self, query, parameters = None):
        current_call_index = len(self.queries)

        self.queries.append(query)
        self.parameters.append(parameters)

        if len(self.output_data) >= current_call_index:
            return self.output_data[current_call_index]
        
        return None

    def get_wdm_data(self, query, parameters):
        return self.run_query(query, parameters)


def test_{{cookiecutter.lambda_name|lower}}_{{cookiecutter.http_method|lower}}():
    wdm_fake = WdmFake()
    {{cookiecutter.lambda_name}} = {{cookiecutter.base_module_name}}.{{cookiecutter.base_class_name}}(wdm_fake)

    # Do work here

    assert False == True