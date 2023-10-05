"""
More from the Cisco devops lab 3.6.6 this time parsing json data
uses pyYAML 3rd party module
"""
import json
import yaml

with open('myfile.json','r') as json_file:
    dict_json = json.load(json_file)

print(type(dict_json))
print(dict_json)
# it is a dictionary, <sarcasm> big surprise </sarcasm>

print("The access token is: {}".format(dict_json['access_token']))
print("The token expires in {} seconds.".format(dict_json['expires_in']))

print("\n----------------")
print(yaml.dump(dict_json))
# conversion of the json to yaml and outputting that to screen

 # function to dump the yaml conversion into a file
with open ('myfile.yaml', 'w') as f:
    f.write(yaml.dump(dict_json))
    print('data written to yaml file')


