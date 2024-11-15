
# This is a mockup of the real python client for Nerve API
# It has the same method signature, but only print out the payload/data
# Original code here: https://github.com/tttech-nerve/nerve-api-examples/blob/master/nerveapi/session.py
# We did not include login, etc., at the moment
def make_request(endpoint:str, method='GET', data=None, files=None, workaround=None) -> str:
    print(f"API was called to {endpoint}:\n{data}")
    return "done"