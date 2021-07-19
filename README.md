This tool can be used to find the vulnerable node packages(npm) for the Dependency Confusion Vulnerability.

To find package.json through Nuclei following command is used:
1. To find from a URL: nuclei -t ./nuclei-templates/exposures/configs/package-json.yaml -u http://demo-app.com:1337
2. To find from a list of URLs: nuclei -t ./nuclei-templates/exposures/configs/package-json.yaml -l {list_of_URLs}

Above package.json can be parsed through this tool to find vulnerable dependency.


Usage:

-> python main.py {package_file_name}

Example:

-> python main.py sample.json



To know more about Dependency Confusion Vulnerabilty, Visit: https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610


Video Resources by @LuD1161(Aseem Shrey): https://youtu.be/P13xrz0EgNw, https://youtu.be/4ggqsJeSu04





