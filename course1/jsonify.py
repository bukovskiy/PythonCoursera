from functools import wraps
import json

def to_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        answer = json.dumps(result)
        return answer
    return wrapper


'''
@to_json
def get_data():
    return None



print(get_data())
'''