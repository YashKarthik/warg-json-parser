import os
import json

t = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
print(json.dumps(t))
