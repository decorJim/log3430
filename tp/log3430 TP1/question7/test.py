import json
import xml.etree.ElementTree as ET

with open("coverage.json") as jsonFile:       # open json file of coverage.py tool
    jsonObject = json.load(jsonFile)            # loads file
    jsonFile.close()

tree = ET.parse('coverage.xml')               # open xml file of pytest.py tool
root = tree.getroot()                           # sets main xml tag as root

filescov = {}                                  # build hashmap with filename as key and line array as value coverage.py
for file in jsonObject['files']:
    filename=file.removeprefix('requests\\')  # remove request/ only get each file name without folder name
    filescov[filename]=jsonObject['files'][file]['executed_lines']

filespytest={}                                # build hashmap with filename as key and line array as value pytest.py
for file in root[1][0][0]:
    lines = []
    for line in file[1]:
        if line.get("hits")=="1":
           lines.append(int(line.get("number")))
        filespytest[file.get("name")] = lines

unique = {}                                # find difference in lines between coverage.py and pytest
for file in filescov:
    set_difference = set(filescov.get(file)) - set(filespytest.get(file))
    list_difference = list(set_difference)
    unique[file] = sorted(list_difference)

with open("linedifferences.json", "w") as outfile:
    json.dump(unique, outfile,indent=4)










