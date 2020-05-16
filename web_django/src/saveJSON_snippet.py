import io
import json

x={}
for i in range(len(df)):
    temp={}
    temp["model"] = "jobs.jobsinfo"
    temp["pk"]= i
    x[i]=temp
    x[i]["fields"]={
        "jobTitle":(df["jobtitle"][i]),
        "description": df["description"][i],
        "place":df["place"][i],
        "link":df["link"][i],
        "site":df["site"][i]}
x=list(x.values())
    
with io.open('test.json', 'w',encoding='windows-1252') as fp:
    json.dump(x,fp)
#Note: My django did not like indents so I got rid of them
