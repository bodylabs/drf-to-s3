class UploadPolicy(object):
    '''
    Encapsulates a policy document for an S3 POST request.

    http://docs.aws.amazon.com/AmazonS3/latest/dev/HTTPPOSTForms.html#HTTPPOSTConstructPolicy

    expiration: The policy expiration date, a native datetime.datetime object
    conditions: A list of UploadPolicyCondition objects
    
    '''
    expiration = None
    conditions = None

    def __init__(self, **kwargs):
        self.expiration = kwargs.get('expiration')
        self.conditions = kwargs.get('conditions')


class UploadPolicyCondition(object):
    '''
    Encapsulates a condition on an UploadPolicy.

    operator: The operator, which is optional. Either 'eq', 'starts-with', or None.
    element_name: The name of the element. A string, required.
    value: For conditions with a single value, the value. Either a string or a number.
    value_range: For conditions with a range, a list containing two values. Either
      value or value_range is required. Defining both is an error.

    '''
    operator = None
    element_name = None
    value = None
    value_range = None

    def __init__(self, **kwargs):
        self.operator = kwargs.get('operator')
        self.element_name = kwargs.get('element_name')
        if kwargs.get('value') is not None and kwargs.get('value_range') is not None:
            raise AssertionError('value and value_range should not both be defined')
        self.value = kwargs.get('value')
        self.value_range = kwargs.get('value_range')
