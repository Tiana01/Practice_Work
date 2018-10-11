import json

from bsread.sender import Sender


def data_generator(p):
    value = p % 100
    data = ({'x': [1, 2, 3], 'y': [value, 1, 2], 'type': 'bar', 'name': 'SF'},
            {'x': [1, value, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'})
    return json.dumps(data)

generator = Sender(port = 15000)



# json_string = json.dumps(data)

# generator.set_pre_function(pre)

# generator.add_channel('ABCH',lambda x: json_string, metadata= {'type': 'string'})
generator.add_channel('ABCH', data_generator , metadata={'type': 'string'})

# generator.set_post_function(pre)

generator.generate_stream()
