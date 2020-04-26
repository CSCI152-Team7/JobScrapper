import json

r = df.to_json(orient='index')
r=json.loads(r)
# r=json.dumps(r, indent=4)
with open('glassdoor.json', 'w') as fp:
    json.dump(r,fp,indent=4)
