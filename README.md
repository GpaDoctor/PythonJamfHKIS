# PythonJemfHKIS

This is a new project using JEMF incooporating with Python using API to monitor and manipulate MACs.

Install the following applications
Assume installed: Python3, git, VS Code is recommended
- pip3 install jps-api-wrapper       jps-api-wrapper       
- pip3 install lxml                  for xml files
- pip3 install pandas                for csv files
- pip3 install openpyxl               for xlsx files

For mac, type the following in terminal
setopt HIST_IGNORE_SPACE
export JPS_USERNAME=yourUsername
export JPS_PASSWORD=yourPassword

For Windows, type the following in terminal
set JPS_USERNAME=yourUsername
set JPS_PASSWORD=yourPassword

specify the path in getdata.py

run the main.py and you are good to go

*Remarks
- INCASE unable to refresh authentication. Restart VS Code completely and retype the authentication.
- INCASE import does not work. Click the bottom right hand corner Python 3.12.4 64-bit. Choose Global, then choose back Recommened.




source:
- https://community.jamf.com/t5/tech-thoughts/introduction-to-jps-api-wrapper-all-in-one-package-for-using-the/ba-p/283126
- https://gitlab.com/cvtc/appleatcvtc/jps-api-wrapper/-/blob/main/README.md#retrieving-the-password-in-python-and-authenticating
- https://jps-api-wrapper.readthedocs.io/en/stable/
- https://developer.jamf.com/jamf-pro/reference/classic-api