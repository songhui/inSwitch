from typing import Literal
# This is a mockup of the real python client for Nerve API
# It has the same method signature, but only print out the payload/data
# Original code here: https://github.com/tttech-nerve/nerve-api-examples/blob/master/nerveapi/session.py
# We did not include login, etc., at the moment
def make_request(endpoint:str, method:Literal['GET', 'POST', 'PUT']='GET', data:str=None, files=None, workaround=None) -> str:
    print(f"PUT: {endpoint}:\n{data}")
    return "done"