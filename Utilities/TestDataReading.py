import os

def load_properties(filename):
    properties = {}
    # Get the absolute path of the properties file
    filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)), filename)

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    with open(filepath, "r") as f:
        for line in f:
            key, value = line.strip().split("=", 1)
            properties[key] = value

    return properties
