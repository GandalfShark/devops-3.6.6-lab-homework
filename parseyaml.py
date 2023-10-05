"""
part 3 of devops homework lab 3.6.6
"""
import json, yaml

with open('myfile.yaml','r') as yaml_file:
    ouryaml = yaml.safe_load(yaml_file)

print(ouryaml, '\n')

print("The access token is {}".format(ouryaml['access_token']))
print("The token expires in {} seconds.".format(ouryaml['expires_in']))
print("\n")
print(json.dumps(ouryaml, indent=4))
