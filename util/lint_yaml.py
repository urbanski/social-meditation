#!/usr/bin/env python3
import os
import sys
import yaml
from yaml import YAMLError

REQUIRED_KEYS = [
    "id",
    "practice",
    "practice.title",
    "practice.creator",
    "practice.format",
    "practice.options",
    "practice.options.category",
    "practice.compression",
    "practice.order",
    "practice.size",
    "references",
]

def lint_yaml_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        
        missing_keys = []
        for key in REQUIRED_KEYS:
            keys = key.split(".")
            current_data = data
            for k in keys:
                if k in current_data:
                    current_data = current_data[k]
                else:
                    missing_keys.append(key)
                    break
        
        if missing_keys:
            print(f"Invalid YAML: {file_path}")
            print(f"Missing keys: {', '.join(missing_keys)}")
            return False
        else:
            print(f"Valid YAML: {file_path}")
            return True

    except YAMLError as e:
        print(f"Invalid YAML: {file_path}")
        print(e)
        return False

def main():
    practices_dir = 'practices'
    success = True
    for root, _, files in os.walk(practices_dir):
        for file in files:
            if file.endswith('.yaml'):
                file_path = os.path.join(root, file)
                if not lint_yaml_file(file_path):
                    success = False
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()