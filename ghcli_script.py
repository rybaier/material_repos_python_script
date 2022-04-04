#module require for running cli commands
import subprocess
#module required for loading json data
import json



#Starter Code (run this code and see what happends!)
# subprocess.call("ls")



#Build out a program similar to the javascript file
repos = open('repo.json')
data = json.load(repos)
for i in data['materials']:
    subprocess.getoutput(i)
    print(i)

repos.close()

print('Repos cloned')
