import json

with open("./test.json") as json_stream:
    json_file = json_stream.read()
    json_content = json.loads(json_file)
    print(json.dumps(json_content, indent=2))
