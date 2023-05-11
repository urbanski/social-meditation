#!/usr/bin/env python3
import sys
import yaml
import jsonschema

if len(sys.argv) != 3:
    print("Usage: validate_yaml.py <input_yaml_file> <schema_yaml_file>")
    sys.exit(1)

# Load the input YAML file
input_yaml_file = sys.argv[1]
with open(input_yaml_file, "r") as f:
    input_yaml = yaml.safe_load(f)

# Load the schema YAML file
schema_yaml_file = sys.argv[2]
with open(schema_yaml_file, "r") as f:
    schema_yaml = yaml.safe_load(f)

# Validate the input YAML file against the schema YAML
jsonschema.validate(input_yaml, schema_yaml)
