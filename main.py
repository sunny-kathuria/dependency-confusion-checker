import requests
import json
import sys
from colorama import Fore,Style

npm_source="https://www.npmjs.com/package/"

fileinput=sys.argv[-1]
package_json_file=open(fileinput)
json_data=json.load(package_json_file)

for dependency in json_data['dependencies']:
    url=npm_source+str(dependency)
    r=requests.get(url=url)
    if(r.status_code==200):
        print(f"{Fore.RED}Dependency: " +str(dependency)+f" is not vulnerable{Style.RESET_ALL}")
    elif(r.status_code==404):
        print(f"{Fore.GREEN}Dependency: " +str(dependency)+f" is vulnerable{Style.RESET_ALL}")
for dependency in json_data['devDependencies']:
    url=npm_source+str(dependency)
    r=requests.get(url=url)
    if(r.status_code==200):
        print(f"{Fore.RED}Dependency: " +str(dependency)+f" is not vulnerable{Style.RESET_ALL}")
    elif(r.status_code==404):
        print(f"{Fore.GREEN}Dependency: " +str(dependency)+f" is vulnerable{Style.RESET_ALL}")



