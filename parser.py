import os
import json

def read_tests_from_file(file_path: str):
    with open(file_path) as json_stream:
        json_file = json_stream.read()
        tests = json.loads(json_file)

        for i, test in enumerate(tests):
            print("Test #", i + 1)
            print("Name: ", test["name"])

            # Perform tests or return array of tests

def read_tests_from_dir(dir_path: str):
    tests = []

    if not os.path.exists(dir_path):
        print(f"Directory '{dir_path}' does not exist.")
        return tests

    for file_name in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file_name)

        if os.path.isfile(file_path) and file_name.endswith(".json"):
            try:
                with open(file_path, 'r') as json_stream:
                    test = json.load(json_stream)
                    tests.append(test)
                    print(f"Parsed {file_name}")

            except json.JSONDecodeError as e:
                print(f"Error parsing {file_name}: {e}")

    print(json.dumps(tests, indent=2))
    return tests # or run tests

read_tests_from_dir("./json_tests/")
