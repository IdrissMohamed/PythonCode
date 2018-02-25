import json

with open('pages/page0.json', 'r') as file:
    contents = ""
    for line in file.readlines():
        contents = contents + line.strip()
    data = json.loads(contents)
    print(data)
    