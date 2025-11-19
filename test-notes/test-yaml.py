import yaml

with open('ieshia.yaml', 'r') as file:
    data = yaml.safe_load(file)

print(data['title'])
print(data['tags'])
print(data["date"])