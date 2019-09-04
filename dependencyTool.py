import subprocess
from subprocess import check_output
import json
success = True
with open('data.json', 'r') as file:
    dependencies = json.loads(file.read())
for dependency,v in dependencies.items():
    command = "pip install " + dependency
    try:
        s = subprocess.check_call(command,shell=True)
    except subprocess.CalledProcessError as e:
        success = False
        print ("failed",command)
if success:
    print("success")