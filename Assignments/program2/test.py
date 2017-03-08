import json

with open("colors.json") as file:
    colors = file.read()

colors = json.loads(colors)

for color in colors:
    print(color)